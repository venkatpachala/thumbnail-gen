from fastapi import APIRouter
from pydantic import BaseModel
from uuid import uuid4
from pathlib import Path
from utils.image_utils import generate_background

router = APIRouter(prefix="/generate-background", tags=["background"])


class PromptRequest(BaseModel):
    prompt: str


@router.post("")
async def create_background(data: PromptRequest):
    filename = Path("backend/uploads") / f"background_{uuid4().hex}.png"
    path = generate_background(data.prompt, str(filename))
    return {"background": str(path)}
