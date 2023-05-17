from __future__ import annotations

import functools
import edgedb
import os
import uuid
# import models
# import schemas

import s3handler, nodes, users, processes, notifications, templates, summary

from fastapi import FastAPI, Request, Response, status, UploadFile, File
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

async def setup_edgedb(app):
    client = app.state.edgedb = edgedb.create_async_client(
        dsn="edgedb://apidemon:12dfYZ_12@edgedb:5656/edgedb",
        tls_security="insecure",
        )
    await client.ensure_connected()

async def shutdown_edgedb(app):
    client, app.state.edgedb = app.state.edgedb, None
    await client.aclose()

app = FastAPI()

app.on_event("startup")(functools.partial(setup_edgedb, app))
app.on_event("shutdown")(functools.partial(shutdown_edgedb, app))

@app.get("/health_check", include_in_schema=False)
async def health_check() -> dict[str, str]:
    return {"status": "Ok"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(DBSessionMiddleware, db_url=os.environ["S3_URL"])

app.include_router(s3handler.router)
app.include_router(nodes.router)
app.include_router(users.router)
app.include_router(processes.router)
app.include_router(notifications.router)
app.include_router(templates.router)
app.include_router(summary.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="IRKUT",
        version="0.0.1",
        description="API для кейса Иркут",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi