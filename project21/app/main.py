from fastapi import FastAPI, Form, File, UploadFile
from pydantic import BaseModel, Field
from typing import Annotated
from fastapi.responses import HTMLResponse
import os
import uuid
import shutil     # Use for multiple file upload 


app = FastAPI()


##HTML form for testing    (Below format use for small filesize )
# @app.get("/", response_class=HTMLResponse)
# async def main():
#     return """
#         <html>
#             <body>
#                 <h2>Single File Upload (bytes)</h2>
#                 <form action="/files/" enctype="multipart/form-data" method="post" >
#                 <input type="file" name="file" >
#                 <input type="submit" value="Upload">
#             </body> 
#         </html>        
#         """

##Using the bytes
# @app.post("/files/")
# async def create_file(file: Annotated[bytes | None, File()] = None):
#     if not file:
#         return {"message": "No file sent"}
#     return ("file Size:", len(file))




## Using the file save in binary name 
# @app.post("/files/")
# async def create_file(file: Annotated[bytes | None, File()] = None):
#     if not file:
#         return {"message": "No file sent"}
    
#     filename = f"{uuid.uuid4()}.bin"
#     save_path = f"uploads/{filename}"

#     os.makedirs("uploads", exist_ok=True)
#     with open(save_path, "wb") as buffer:
#         buffer.write(file)  
#     return {"File Size:", len(file)}




## Using Uploadfile 
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
        <html>
            <body>
                 <h2>Single File Upload (Uploadfiles)</h2>
                <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
                <input type="file" name="file">
                <input type="submit" value="Upload">
            </body> 
        </html>        
        """

@app.post("/uploadfiles/")
async def create_upload_file(file: Annotated[UploadFile | None, File()] = None):
    if not file:
        return {"message": "No upload file sent"}
    
    save_path = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "content_type": file.content_type}


    

    
