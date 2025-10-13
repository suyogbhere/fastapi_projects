from fastapi import FastAPI, Form, File, UploadFile
from pydantic import BaseModel, Field
from typing import Annotated
from fastapi.responses import HTMLResponse


app = FastAPI()


##HTML form for testing    (Below format use for small filesize )
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
        <html>
            <body>
                <h2>Single File Upload (bytes)</h2>
                <form action="/files/" enctype="multipart/form-data" method="post" >
                <input type="file" name="file" >
                <input type="submit" value="Upload">
            </body> 
        </html>        
        """


@app.post("/files/")
async def create_file(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"message": "No file sent"}
    return ("file Size:", len(file))