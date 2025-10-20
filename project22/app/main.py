from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from fastapi.responses import HTMLResponse
import os
import shutil


app = FastAPI()


## Using Uploadfile 
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
        <html>
            <body>
                 <h2>Multiple File Upload (Uploadfiles)</h2>
                <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
                <input type="file" name="files" multiple>
                <input type="submit" value="Upload">
                </form>
            </body> 
        </html>        
        """


@app.post("/uploadfiles/")
async def create_upload_file(files: Annotated[list[UploadFile], File()]):
    save_file = []
    os.makedirs("uploads", exist_ok=True)
    for file in files:
        save_path = f"uploads/{file.filename}"
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        save_file.append({"filename": file.filename})
    return save_file    



