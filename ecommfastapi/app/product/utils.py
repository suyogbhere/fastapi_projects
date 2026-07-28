from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile
from slugify import slugify


UPLOAD_DIR = Path("media")
UPLOAD_DIR.mkdir(exist_ok=True)


async def save_upload_file(upload_file: UploadFile, sub_dir: str) -> str:
    ext = Path(upload_file.filename).suffix
    filename = f"{uuid4().hex}{ext}"
    print("FILENAME:", filename)
    dir_path = UPLOAD_DIR/ sub_dir
    print("DIR_PATH:", dir_path)
    dir_path.mkdir(parents=True, exist_ok=True)
    file_path = dir_path / filename
    print("FILE PATH:", file_path)

    content = await upload_file.read()
    with file_path.open("wb") as f:
        f.write(content)

    return str(file_path)


def generate_slug(text: str) -> str:
    return slugify(text)