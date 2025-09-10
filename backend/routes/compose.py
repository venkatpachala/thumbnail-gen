from fastapi import APIRouter
from pydantic import BaseModel
from uuid import uuid4
from pathlib import Path
from utils.image_utils import compose_thumbnail

router = APIRouter(prefix="/compose-thumbnail", tags=["compose"])


class ComposeRequest(BaseModel):
    background: str
    cutout: str
    text: str


@router.post("")
async def compose(data: ComposeRequest):
    out_path = Path("backend/uploads") / f"thumbnail_{uuid4().hex}.png"
    compose_thumbnail(data.background, data.cutout, data.text, str(out_path))
    return {"thumbnail": str(out_path)}
