from __future__ import annotations

from http import HTTPStatus
from typing import List

import os
import models
import edgedb
import uuid
from fastapi import APIRouter, Depends, HTTPException, Query, File, UploadFile
from pydantic import BaseModel
from fastapi.responses import FileResponse

from __init__ import get_edgedb_client
from fastapi_sqlalchemy import db
import queries.get_processes_by_group_async_edgeql as get_processes_group_qry
import queries.get_processes_by_realiser_async_edgeql as get_processes_realiser_qry
import queries.update_assigned_notification_async_edgeql as update_assigned_qry
import queries.update_process_node_status_async_edgeql as update_status_qry
import queries.update_passport_ref_async_edgeql as update_ref_qry
import queries.get_process_by_id_async_edgeql as get_process_id_qry

router = APIRouter()

class ProcessData(BaseModel):
    login: str

class ProcessData2(BaseModel):
    id: uuid.UUID

@router.post("/processes/group")
async def get_processes_group(
    # login: str = Query(None, max_length=50),
    data: ProcessData,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
) -> List[get_processes_group_qry.GetProcessesByGroupResult] | get_processes_group_qry.GetProcessesByGroupResult:
    try:
        process = await get_processes_group_qry.get_processes_by_group(client, login=data.login)
        return [{
            "id": process[i].id,
            "title": process[i].title,
            "realiser": {"id": process[i].realiser.id,
                         "login": process[i].realiser.login},
            "realiser_group": {"id": process[i].realiserGroup.id,
                               "title": process[i].realiserGroup.title,
                               "boss": {"login": process[i].realiserGroup.boss.login},
                               "staff": [{"login": process[i].realiserGroup.staff[j].login} for j in range(len(process[i].realiserGroup.staff))],
                               },
            "priority": process[i].priority.value,
            "passport_ref": process[i].passport_ref,
            "process_type": {"title": process[i].processType.title},
            "nodes": [{"id": process[i].nodes[j].id,
                       "title": process[i].nodes[j].title,
                       "assigned": [
                           {"id": process[i].nodes[j].assigned[k].id,
                            "title": process[i].nodes[j].assigned[k].title,
                            "boss": {"login": process[i].nodes[j].assigned[k].boss.login},
                            "staff": [{"login": process[i].nodes[j].assigned[k].staff[l].login} for l in range(len(process[i].nodes[j].assigned[k].staff))],
                            }
                       for k in range(len(process[i].nodes[j].assigned))],
                       "along": {"id": process[i].nodes[j].along.id,
                                 "title": process[i].nodes[j].along.title,
                                 "addenable": process[i].nodes[j].along.addenable,
                                 } if process[i].nodes[j].along != None else None,
                        "addenable": False,
                        "subs": [{"id": process[i].nodes[j].subs[k].id,
                                  "title": process[i].nodes[j].subs[k].title,
                                  "start_verification": process[i].nodes[j].subs[k].start_verification,
                                  "comments": [{"text_str": process[i].nodes[j].subs[k].comments[l].text_str,
                                                "author": process[i].nodes[j].subs[k].comments[l].author.id,
                                                "answer": process[i].nodes[j].subs[k].comments[l].answer
                                                } for l in range(len(process[i].nodes[j].subs[k].comments))] if process[i].nodes[j].subs[k].comments != None else None,
                                    "fit": {"id": process[i].nodes[j].subs[k].fit.id,
                                            "login": process[i].nodes[j].subs[k].fit.login,
                                            "FIO": process[i].nodes[j].subs[k].fit.FIO,
                                            "rights": [
                                                process[i].nodes[j].subs[k].fit.rights[l].value
                                                  for l in range(len(process[i].nodes[j].subs[k].fit.rights))]
                                    } if process[i].nodes[j].subs[k].fit != None else None,
                                    "end_verification": process[i].nodes[j].subs[k].end_verification,
                                    "end_correction": process[i].nodes[j].subs[k].end_correction,
                                  } 
                                  for k in range(len(process[i].nodes[j].subs))],
                        "next": process[i].nodes[j].next.id if process[i].nodes[j].next != None else None,
                        "status": {"title": process[i].nodes[j].status.title,
                                   "color": process[i].nodes[j].status.color} if process[i].nodes[j].status != None else None,
                        "receipt": process[i].nodes[j].receipt,
                       } 
                      for j in range(len(process[i].nodes))]
            }
            for i in range(len(process))]
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )

@router.post("/processes/realiser")
async def get_processes_group(
    # login: str = Query(None, max_length=50),
    data: ProcessData,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
) -> List[get_processes_realiser_qry.GetProcessesByRealiserResult] | get_processes_realiser_qry.GetProcessesByRealiserResult:
    try:
        process = await get_processes_realiser_qry.get_processes_by_realiser(client, realiser_login=data.login)
        return [{
            "id": process[i].id,
            "title": process[i].title,
            "realiser": {"id": process[i].realiser.id,
                         "login": process[i].realiser.login},
            "realiser_group": {"id": process[i].realiserGroup.id,
                               "title": process[i].realiserGroup.title,
                               "boss": {"login": process[i].realiserGroup.boss.login},
                               "staff": [{"login": process[i].realiserGroup.staff[j].login} for j in range(len(process[i].realiserGroup.staff))],
                               },
            "priority": process[i].priority.value,
            "passport_ref": process[i].passport_ref,
            "process_type": {"title": process[i].processType.title},
            "nodes": [{"id": process[i].nodes[j].id,
                       "title": process[i].nodes[j].title,
                       "assigned": [
                           {"id": process[i].nodes[j].assigned[k].id,
                            "title": process[i].nodes[j].assigned[k].title,
                            "boss": {"login": process[i].nodes[j].assigned[k].boss.login},
                            "staff": [{"login": process[i].nodes[j].assigned[k].staff[l].login} for l in range(len(process[i].nodes[j].assigned[k].staff))],
                            }
                       for k in range(len(process[i].nodes[j].assigned))],
                       "along": {"id": process[i].nodes[j].along.id,
                                 "title": process[i].nodes[j].along.title,
                                 "addenable": process[i].nodes[j].along.addenable,
                                 } if process[i].nodes[j].along != None else None,
                        "addenable": False,
                        "subs": [{"id": process[i].nodes[j].subs[k].id,
                                  "title": process[i].nodes[j].subs[k].title,
                                  "start_verification": process[i].nodes[j].subs[k].start_verification,
                                  "comments": [{"text_str": process[i].nodes[j].subs[k].comments[l].text_str,
                                                "author": process[i].nodes[j].subs[k].comments[l].author.id,
                                                "answer": process[i].nodes[j].subs[k].comments[l].answer
                                                } for l in range(len(process[i].nodes[j].subs[k].comments))] if process[i].nodes[j].subs[k].comments != None else None,
                                    "fit": {"id": process[i].nodes[j].subs[k].fit.id,
                                            "login": process[i].nodes[j].subs[k].fit.login,
                                            "FIO": process[i].nodes[j].subs[k].fit.FIO,
                                            "rights": [
                                                process[i].nodes[j].subs[k].fit.rights[l].value
                                                  for l in range(len(process[i].nodes[j].subs[k].fit.rights))]
                                    } if process[i].nodes[j].subs[k].fit != None else None,
                                    "end_verification": process[i].nodes[j].subs[k].end_verification,
                                    "end_correction": process[i].nodes[j].subs[k].end_correction,
                                  } 
                                  for k in range(len(process[i].nodes[j].subs))],
                        "next": process[i].nodes[j].next.id if process[i].nodes[j].next != None else None,
                        "status": {"title": process[i].nodes[j].status.title,
                                   "color": process[i].nodes[j].status.color} if process[i].nodes[j].status != None else None,
                        "receipt": process[i].nodes[j].receipt,
                       } 
                      for j in range(len(process[i].nodes))]
            }
            for i in range(len(process))]
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )

@router.post("/processes/id")
async def get_process_by_id(
    data: ProcessData2,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
):
    try:
        process = await get_process_id_qry.get_process_by_id(client, process_id=data.id)
        return {
            "id": process.id,
            "title": process.title,
            "realiser": {"id": process.realiser.id,
                         "login": process.realiser.login},
            "realiser_group": {"id": process.realiserGroup.id,
                               "title": process.realiserGroup.title,
                               "boss": {"login": process.realiserGroup.boss.login},
                               "staff": [{"login": process.realiserGroup.staff[j].login} for j in range(len(process.realiserGroup.staff))],
                               },
            "priority": process.priority.value,
            "passport_ref": process.passport_ref,
            "process_type": {"title": process.processType.title},
            "nodes": [{"id": process.nodes[j].id,
                       "title": process.nodes[j].title,
                       "assigned": [
                           {"id": process.nodes[j].assigned[k].id,
                            "title": process.nodes[j].assigned[k].title,
                            "boss": {"login": process.nodes[j].assigned[k].boss.login},
                            "staff": [{"login": process.nodes[j].assigned[k].staff[l].login} for l in range(len(process.nodes[j].assigned[k].staff))],
                            }
                       for k in range(len(process.nodes[j].assigned))],
                       "along": {"id": process.nodes[j].along.id,
                                 "title": process.nodes[j].along.title,
                                 "addenable": process.nodes[j].along.addenable,
                                 } if process.nodes[j].along != None else None,
                        "addenable": False,
                        "subs": [{"id": process.nodes[j].subs[k].id,
                                  "title": process.nodes[j].subs[k].title,
                                  "start_verification": process.nodes[j].subs[k].start_verification,
                                  "comments": [{"text_str": process.nodes[j].subs[k].comments[l].text_str,
                                                "author": process.nodes[j].subs[k].comments[l].author.id,
                                                "answer": process.nodes[j].subs[k].comments[l].answer
                                                } for l in range(len(process.nodes[j].subs[k].comments))] if process.nodes[j].subs[k].comments != None else None,
                                    "fit": {"id": process.nodes[j].subs[k].fit.id,
                                            "login": process.nodes[j].subs[k].fit.login,
                                            "FIO": process.nodes[j].subs[k].fit.FIO,
                                            "rights": [
                                                process.nodes[j].subs[k].fit.rights[l].value
                                                  for l in range(len(process.nodes[j].subs[k].fit.rights))]
                                    } if process.nodes[j].subs[k].fit != None else None,
                                    "end_verification": process.nodes[j].subs[k].end_verification,
                                    "end_correction": process.nodes[j].subs[k].end_correction,
                                  } 
                                  for k in range(len(process.nodes[j].subs))],
                        "next": process.nodes[j].next.id if process.nodes[j].next != None else None,
                        "status": {"title": process.nodes[j].status.title,
                                   "color": process.nodes[j].status.color} if process.nodes[j].status != None else None,
                        "receipt": process.nodes[j].receipt,
                       } 
                      for j in range(len(process.nodes))]
            }  
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        ) 

## убрать роут, объединить с download_pdf
# @router.post("/processes/update_status")
# async def update_status(
#     # process_id: uuid.UUID,
#     data: ProcessData2,
#     client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
# ):
#     try:
#         updated_status = await update_status_qry.update_process_node_status(
#             client,
#             process_id=data.id,
#         )
#         updated_notification = await update_assigned_qry.update_assigned_notification(
#             client,
#             process_id=data.id,
#         )
#         return {
#             "status": [{"id": updated_status[i].id} for i in range(len(updated_status))],
#             "notification": [{"id": updated_notification[i].id} for i in range(len(updated_notification))],
#         }
#     except edgedb.errors.InvalidValueError:
#         raise HTTPException(
#             status_code=HTTPStatus.BAD_REQUEST,
#             detail={
#                 "error": "Invalid request",
#             },
#         )
    
@router.post("/processes/update_passport")
async def update_right(process_id: uuid.UUID,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client), file: UploadFile = File(...)):
    file_bytes = await file.read()
    s3_file = models.Result(
        file_name=file.filename, 
        file_data=file_bytes,
    )
    db.session.add(s3_file)
    try:
        updated_status = await update_status_qry.update_process_node_status(
            client,
            process_id=process_id,
        )
        updated_notification = await update_assigned_qry.update_assigned_notification(
            client,
            process_id=process_id,
        )
        updated_ref = await update_ref_qry.update_passport_ref(
            client,
            process_id=process_id,
            passport_ref=file.filename,
        )
        return {
            "status": [{"id": updated_status[i].id} for i in range(len(updated_status))],
            "notification": [{"id": updated_notification[i].id} for i in range(len(updated_notification))],
            "updated_ref": updated_ref.passport_ref,
        }
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )