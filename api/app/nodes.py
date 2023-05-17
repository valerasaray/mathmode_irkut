from __future__ import annotations

from http import HTTPStatus
from typing import List

import edgedb
import uuid
import datetime
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from pytz import timezone
from __init__ import get_edgedb_client

import queries.create_along_node_async_edgeql as create_along_node_qry
import queries.select_node_by_assigned_group_async_edgeql as get_node_assigned_qry
import queries.update_node_status_async_edgeql as update_node_status_qry
import queries.update_subnode_fit_async_edgeql as update_node_fit_qry
import queries.update_subnode_end_correction_async_edgeql as update_end_correction_qry
import queries.update_subnode_end_validation_async_edgeql as update_end_validation_qry
import queries.update_status_node_async_edgeql as update_status_node_qry
import queries.get_father_along_node_async_edgeql as get_father_along_node_qry
import queries.get_node_by_id_async_edgeql as get_node_by_id_qry
import queries.start_node_async_edgeql as start_node_qry
import queries.create_assigned_notifications_async_edgeql as create_assigned_notifications_qry

router = APIRouter()

class AlongData(BaseModel):
    title: str
    department_id: uuid.UUID
    node_id: uuid.UUID

class FigData(BaseModel):
    login: str
    subnode_id: uuid.UUID

class UpdateData(BaseModel):
    subnode_id: uuid.UUID
    date: datetime.datetime

class CompleteNodeData(BaseModel):
    node_id: uuid.UUID

class SelectedNodeData(BaseModel):
    login: str

@router.post("/nodes/along")
async def post_along_node(
    data: AlongData,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
) -> create_along_node_qry.CreateAlongNodeResult:
    try:
        created_node = await create_along_node_qry.create_along_node(
            client,
            title=data.title,
            department_id=data.department_id,
            node_id=data.node_id,
        )
        return {
            "id": created_node.along.id,
            "title": created_node.along.title,
        }
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )

@router.post("/nodes/update_fig")
async def update_fig(
    data: FigData,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
):
    try:
        updated_node = await update_node_status_qry.update_node_status(
            client,
            subnode_id=data.subnode_id,
        )
        if updated_node[0] != None:
            if updated_node[0].subs != None:
                if updated_node[0].subs[0].fit == None:
                    updated_fit = await update_node_fit_qry.update_subnode_fit(
                        client,
                        login=data.login,
                        subnode_id=data.subnode_id,
                    )
                    return {
                        "id": updated_fit.id,
                    }
                else:
                    return [{
                        "id": updated_node[i].id,
                        "fit": [updated_node[i].subs[j].fit if updated_node[i].subs != None else None for j in range(len(updated_node[i].subs))
                    ]} for i in range(len(updated_node))]
            else:
                return [{
                        "id": updated_node[i].id,
                        "fit": [updated_node[i].subs[j].fit if updated_node[i].subs != None else None for j in range(len(updated_node[i].subs))
                    ]} for i in range(len(updated_node))]
        else:
            return [{
                        "id": updated_node[i].id,
                        "fit": [updated_node[i].subs[j].fit if updated_node[i].subs != None else None for j in range(len(updated_node[i].subs))
                    ]} for i in range(len(updated_node))]
        
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )
    
@router.post("/nodes/up_end_ver")
async def update_end_verification(
    data: UpdateData,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
) -> update_end_validation_qry.UpdateSubnodeEndValidationResult | None:
    try:
        end_ver = await update_end_validation_qry.update_subnode_end_validation(
            client,
            subnode_id=data.subnode_id,
            datetime=data.date
        )
        return {
            "id": end_ver.id
        }
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )

@router.post("/nodes/up_end_cor")
async def update_end_correction(
    data: UpdateData,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
) -> update_end_correction_qry.UpdateSubnodeEndCorrectionResult | None:
    try:
        end_ver = await update_end_correction_qry.update_subnode_end_correction(
            client,
            subnode_id=data.subnode_id,
            datetime=data.date
        )
        return {
            "id": end_ver.id
        }
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )


@router.post("/nodes/by_assigned")
async def get_nodes_by_assigned(
    # login: str = Query(None, max_length=50),
    data: SelectedNodeData,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
) -> List[get_node_assigned_qry.SelectNodeByAssignedGroupResult] | get_node_assigned_qry.SelectNodeByAssignedGroupResult:
    try:
        nodes = await get_node_assigned_qry.select_node_by_assigned_group(client, login=data.login)
        return [{"id": nodes[j].id,
                       "title": nodes[j].title,
                       "assigned": [
                           {"id": nodes[j].assigned[k].id,
                            "title": nodes[j].assigned[k].title,
                            "boss": {"login": nodes[j].assigned[k].boss.login},
                            "staff": [{"login": nodes[j].assigned[k].staff[l].login} for l in range(len(nodes[j].assigned[k].staff))],
                            }
                       for k in range(len(nodes[j].assigned))],
                       "along": {"id": nodes[j].along.id,
                                 "title": nodes[j].along.title,
                                 "addenable": nodes[j].along.addenable,
                                 } if nodes[j].along != None else None,
                        "addenable": False,
                        "subs": [{"id": nodes[j].subs[k].id,
                                  "title": nodes[j].subs[k].title,
                                  "start_verification": nodes[j].subs[k].start_verification,
                                  "comments": [{"text_str": nodes[j].subs[k].comments[l].text_str,
                                                "author": nodes[j].subs[k].comments[l].author.id,
                                                "answer": nodes[j].subs[k].comments[l].answer
                                                } for l in range(len(nodes[j].subs[k].comments))] if nodes[j].subs[k].comments != None else None,
                                    "fit": {"id": nodes[j].subs[k].fit.id,
                                            "login": nodes[j].subs[k].fit.login,
                                            "FIO": nodes[j].subs[k].fit.FIO,
                                            "rights": [
                                                nodes[j].subs[k].fit.rights[l].value
                                                  for l in range(len(nodes[j].subs[k].fit.rights))]
                                    } if nodes[j].subs[k].fit != None else None,
                                    "end_verification": nodes[j].subs[k].end_verification,
                                    "end_correction": nodes[j].subs[k].end_correction,
                                  } 
                                  for k in range(len(nodes[j].subs))],
                        "next": nodes[j].next.id if nodes[j].next != None else None,
                        "status": {"title": nodes[j].status.title,
                                   "color": nodes[j].status.color} if nodes[j].status != None else None,
                        "receipt": nodes[j].receipt,
                       } 
                      for j in range(len(nodes))]
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )

@router.post("/nodes/complete")
async def post_complete_node(
    data: CompleteNodeData,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
):
    try:
        node = await update_status_node_qry.update_status_node(client, node_id=data.node_id, new_status_title="Проверено")

        step_right_success = True
        rnode = node
        while rnode.along != None:
            rnode = await get_node_by_id_qry.get_node_by_id(client, node_id=rnode.along.id)
            if rnode.status != None:
                if rnode.status.title != "Проверено":
                    step_right_success = False
                    break
            else:
                step_right_success = False
                break

        step_left_success = True
        lnode = await get_father_along_node_qry.get_father_along_node(client, node_id=node.id)
        while lnode != None:
            if lnode.status != None:
                if lnode.status.title != "Проверено":
                    step_left_success = False
                    break
            else:
                step_left_success = False
                break
            lnode = await get_father_along_node_qry.get_father_along_node(client, node_id=lnode.id)

        if step_left_success and step_right_success:
            rnode = node
            while rnode.along != None:
                rnode = await get_node_by_id_qry.get_node_by_id(client, node_id=rnode.along.id)
                if rnode.next != None:
                    await start_next_node(client=client, node_id=rnode.next.id)
                print("rkal ", rnode)
            lnode = await get_father_along_node_qry.get_father_along_node(client, node_id=node.id)
            while lnode != None:
                if lnode.next != None:
                    await start_next_node(client=client, node_id=lnode.next.id)
                lnode = await get_father_along_node_qry.get_father_along_node(client, node_id=lnode.id)
                print("lkal ", lnode)
            if node.next != None:
                await start_next_node(client=client, node_id=node.next.id)
        return {
            "id": node.id
        }
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )

async def start_next_node(
    node_id: uuid.UUID,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client)
):
    node = await get_node_by_id_qry.get_node_by_id(client, node_id=node_id)
    print(node)
    if node.status != None:
        return
    else:
        await start_node_qry.start_node(client, node_id=node_id, rec_time=datetime.datetime.now(timezone('Europe/Moscow')), new_status_title="Принято на проверку")
        await create_assigned_notifications_qry.create_assigned_notifications(client, node_id=node_id)

    if node.along != None:
        await start_next_node(client=client, node_id=node.along.id)
    