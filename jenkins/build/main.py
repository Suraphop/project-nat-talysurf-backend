from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File, UploadFile
from typing import List
from ftp import ftp_upload,mfg_date
import pandas as pd
import tempfile

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def index():
    """print hello world"""
    return {"result": "csv to ftp server: versions 1.0.0"}

@app.get("/files")
def files():
    """return file"""
    result = [{"name": "test.csv","url":"http://localhost:9090/files/test.csv"}]
    return result

@app.post("/upload")
def upload(files: List[UploadFile] = File(...)):
    for file in files:
        try:
            project_path = 'talysurf'
            ftp_upload(project_path,file.file)
        except Exception as e:
            return {"message": f"There was an error uploading the file(s),{e}"}
        finally:
            file.file.close()
    return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}
