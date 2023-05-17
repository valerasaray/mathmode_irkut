import edgedb
from fastapi import Request


def get_edgedb_client(request: Request) -> edgedb.AsyncIOClient:
    return request.app.state.edgedb

# async def get_edgedb_client(db_url: str) -> edgedb.AsyncIOClient:
#     return await edgedb.async_connect(dsn=db_url)
