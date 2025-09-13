from fastapi import FastAPI

app = FastAPI()


##Path Converter
@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return {"You requested file path is ": file_path}

