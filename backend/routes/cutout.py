from fastapi import APIRouter, UploadFile, File
from uuid import uuid4
from pathlib import Path
from utils.image_utils import cutout_photo

router = APIRouter(prefix="/cutout-photo", tags=["cutout"])


@router.post("")
async def create_cutout(file: UploadFile = File(...)):
    temp_name = Path("backend/uploads") / f"upload_{uuid4().hex}_{file.filename}"
    temp_name.parent.mkdir(parents=True, exist_ok=True)
    with open(temp_name, "wb") as f:
        f.write(await file.read())
    out_path = Path("backend/uploads") / f"cutout_{uuid4().hex}.png"
    cutout_photo(str(temp_name), str(out_path))
    return {"cutout": str(out_path)}
