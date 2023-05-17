from __future__ import annotations

from http import HTTPStatus
from typing import List

import edgedb
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
# from fastapi.encoders import jsonable_encoder

from __init__ import get_edgedb_client

import queries.get_user_by_login_async_edgeql as get_user_by_login_qry

router = APIRouter()

class UserData(BaseModel):
    login: str

@router.post("/user")
async def get_user(
    data: UserData,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
) -> List[get_user_by_login_qry.GetUserByLoginResult] | get_user_by_login_qry.GetUserByLoginResult:
    try:
        user = await get_user_by_login_qry.get_user_by_login(client, login=data.login)
        return {
            "id": user.id,
            "login": user.login,
            "rights": [{"value": user.rights[i].value if user.rights[i] != None else None} 
                       for i in range(len(user.rights))],
        }
    except edgedb.errors.InvalidValueError:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail={
                "error": "Invalid request",
            },
        )
