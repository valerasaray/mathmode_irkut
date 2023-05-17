from __future__ import annotations

from http import HTTPStatus
from typing import List

import edgedb
import uuid
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
import json

from __init__ import get_edgedb_client

import queries.get_notification_by_group_async_edgeql as get_notification_by_group_qry
import queries.get_notification_by_user_async_edgeql as get_notification_by_user_qry
import queries.update_comments_notification_async_edgeql as update_comment_notification_qry
import queries.create_comments_notification_async_edgeql as create_comment_notification_qry

router = APIRouter()

class CommentsDataUpdate(BaseModel):
    login: str
    answer: str
    comment_id: uuid.UUID

class CommentsDataCreate(BaseModel):
    login: str
    text_str: str
    subnode_id: uuid.UUID

class NotificationData(BaseModel):
    login: str

@router.post("/notifications")
async def get_notifications(
    # login: str = Query(None, max_length=50),
    data: NotificationData,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
):
    try:
        notification_1 = await get_notification_by_user_qry.get_notification_by_user(client, login=data.login)
        notification_2 = await get_notification_by_group_qry.get_notification_by_group(client, login=data.login)
        return {
            "notification_user": [{"user_to": {
                                       "id": notification_1[i].user_to.id,
                                        "login": notification_1[i].user_to.login,
                                        "rights": [notification_1[i].user_to.rights[j].value 
                                                   for j in range(len(notification_1[i].user_to.rights))
                                                   ]
                                    } if notification_1[i].user_to != None else None,
                                   "to_department": {
                                       "id": notification_1[i].to_department.id,
                                        "title": notification_1[i].to_department.title
                                    } if notification_1[i].to_department != None else None,
                                    "comment": {
                                        "id": notification_1[i].comment.id,
                                        "text_str": notification_1[i].comment.text_str,
                                        "author": {
                                            "id": notification_1[i].comment.author.id,
                                            "login": notification_1[i].comment.author.login,
                                            "rights": [notification_1[i].comment.author.rights[j].value 
                                                   for j in range(len(notification_1[i].comment.author.rights))
                                                   ],
                                        },
                                        "answer": notification_1[i].comment.answer,
                                    } if notification_1[i].comment != None else None,
                                    "new_assign": notification_1[i].new_assign.id if notification_1[i].new_assign != None else None,
                                    "passed_node": [notification_1[i].passed_node[j].id for j in range(len(notification_1[i].passed_node))] if notification_1[i].passed_node != None else None,
                                   }
                                  for i in range(len(notification_1))],
            "notification_group": [{"user_to": {
                                       "id": notification_2[i].user_to.id,
                                        "login": notification_2[i].user_to.login,
                                        "rights": [notification_2[i].user_to.rights[j].value 
                                                   for j in range(len(notification_2[i].user_to.rights))
                                                   ]
                                    } if notification_2[i].user_to != None else None,
                                   "to_department": {
                                       "id": notification_2[i].to_department.id,
                                        "title": notification_2[i].to_department.title
                                    } if notification_2[i].to_department != None else None,
                                    "comment": {
                                        "id": notification_2[i].comment.id,
                                        "text_str": notification_2[i].comment.text_str,
                                        "author": {
                                            "id": notification_2[i].comment.author.id,
                                            "login": notification_2[i].comment.author.login,
                                            "rights": [notification_2[i].comment.author.rights[j].value 
                                                   for j in range(len(notification_2[i].comment.author.rights))
                                                   ],
                                        },
                                        "answer": notification_2[i].comment.answer,
                                    } if notification_2[i].comment != None else None,
                                    "new_assign": notification_2[i].new_assign.id if notification_2[i].new_assign != None else None,
                                    "passed_node": [notification_2[i].passed_node[j].id for j in range(len(notification_2[i].passed_node))] if notification_2[i].passed_node != None else None,
                                   }
                                  for i in range(len(notification_2))],
        }
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )
    
@router.post("/comments/update")
async def update_comment(
    data: CommentsDataUpdate,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
):
    try:
        res = await update_comment_notification_qry.update_comments_notification(
            client,
            login=data.login,
            comment_id=data.comment_id,
            answer=data.answer,
        )
        return {
            "id": res.id, 
            "comment": {
                "id": res.comment.id,
                "author": res.comment.author.login,
                "text_str": res.comment.text_str,
                "answer": res.comment.answer,
            } if res.comment != None else None
        }
        
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )
    
@router.post("/comments/create")
async def create_comment(
    data: CommentsDataCreate,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
):
    try:
        res = await create_comment_notification_qry.create_comments_notification(
            client,
            login=data.login,
            subnode_id=data.subnode_id,
            text_str=data.text_str,
        )
        return {
            "id": res.id, 
            "comment": {
                "id": res.comment.id,
                "author": res.comment.author.login,
                "text_str": res.comment.text_str,
                "answer": res.comment.answer,
            } if res.comment != None else None
        }
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )
