import os
import models

from fastapi import APIRouter, Depends, HTTPException, Query, File, UploadFile
from fastapi.responses import FileResponse
from fastapi_sqlalchemy import db

from pydantic import BaseModel

router = APIRouter()

class MyData(BaseModel):
    file_name: str

@router.post("/s3/upload")
async def upload_file(file: UploadFile = File(...)):
    file_bytes = await file.read()
    s3_file = models.Result(
        file_name=file.filename, 
        file_data=file_bytes,
    )
    db.session.add(s3_file)
    db.session.commit()
    return {"filename": file.filename}

@router.post("/s3/download")
async def download_file(
    # file_name: str
    data: MyData
    ):
    file_path = os.path.abspath(data.file_name)
    file = db.session.query(models.Result).filter_by(file_name=data.file_name).first()
    if (file is None):
        return {"error": "File not found"}
    with open(data.file_name, "wb") as f:
        f.write(file.file_data)
    return FileResponse(path=file_path, filename=data.file_name, media_type="application/pdf")