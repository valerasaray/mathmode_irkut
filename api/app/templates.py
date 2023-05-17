from __future__ import annotations

from http import HTTPStatus
from typing import List

import edgedb
import uuid
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel

from __init__ import get_edgedb_client

import queries.create_new_process_from_template_async_edgeql as create_new_process_from_template_qry
import queries.get_node_by_id_async_edgeql as get_node_by_id_qry
import queries.create_new_node_async_edgeql as create_new_node_qry
import queries.update_node_along_async_edgeql as update_node_along_qry
import queries.update_node_next_async_edgeql as update_node_next_qry
import queries.add_node_to_process_async_edgeql as add_node_to_process_qry
import queries.get_process_from_template_async_edgeql as get_process_from_template_qly
import queries.copy_subnodes_node_to_node_async_edgeql as copy_subnodes_node_to_node_qly
import queries.update_process_head_node_async_edgeql as update_process_head_node_qly
import queries.get_templates_async_edgeql as get_templates_qry

router = APIRouter()

class CreateProcessData(BaseModel):
    template_id: uuid.UUID
    department_id: uuid.UUID
    title: str
    priority_id: uuid.UUID
    login: str


async def clone_template_nodes(
    temp_node_id: uuid.UUID,
    used: uuid.UUID, new_process_id: uuid.UUID,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
):
    if temp_node_id in used:
        return None
    
    used.add(temp_node_id)
    temp_info = await get_node_by_id_qry.get_node_by_id(
        client,
        node_id=temp_node_id
    )
    addentable = False
    if temp_info.addenable != None:
        addentable=temp_info.addenable
    new_node = await create_new_node_qry.create_new_node(
        client,
        title=temp_info.title,
        addentable=addentable
    )
    await copy_subnodes_node_to_node_qly.copy_subnodes_node_to_node(client, temp_node_id=temp_info.id, node_id=new_node.id)
    if temp_info.next != None:
        next_id = await clone_template_nodes(
            client=client, 
            new_process_id=new_process_id,
            used=used,
            temp_node_id=temp_info.next.id
        )
        await update_node_next_qry.update_node_next(client, node_id=new_node.id, next_id=next_id)
    if temp_info.along != None:
        along_id = await clone_template_nodes(
            client=client,
            new_process_id=new_process_id,
            used=used,
            temp_node_id=temp_info.along.id
        )
        await update_node_along_qry.update_node_along(client, node_id=new_node.id, along_id=along_id)

    await add_node_to_process_qry.add_node_to_process(client, node_id=new_node.id, process_id=new_process_id)
    # добавляем ноду в процесс
    return new_node.id

@router.post("/templates/create")
async def post_create_templates(
    data: CreateProcessData,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
):
    try:
        new_process = await create_new_process_from_template_qry.create_new_process_from_template(
            client,
            template_id=data.template_id,
            login=data.login,
            passport_ref=data.title,
            department_id=data.department_id,
            priority_id=data.priority_id        
        )
        template = await get_process_from_template_qly.get_process_from_template(client, template_id=data.template_id)
        used = set()
        head_id = await clone_template_nodes(template.process.head.id, used, new_process.id, client)
        await update_process_head_node_qly.update_process_head_node(
            client, head_id=head_id, process_id=new_process.id
        )

        return {"head_id": head_id} 
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )

@router.get("/templates")
async def get_temlates(
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
):
    templates = await get_templates_qry.get_templates(client)
    return [{"id": templates[i].id, "title": templates[i].title} for i in range(len(templates))]