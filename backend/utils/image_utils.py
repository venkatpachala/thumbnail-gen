from diffusers import StableDiffusionPipeline
import torch
from rembg import remove
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


def generate_background(prompt: str, out_path: str) -> str:
    """Generate a background image from text using Stable Diffusion."""
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = pipe.to(device)
    pipe.enable_attention_slicing()
    pipe.enable_sequential_cpu_offload()
    image = pipe(prompt, height=512, width=512).images[0]
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    image.save(out_path)
    return out_path


def cutout_photo(input_path: str, out_path: str) -> str:
    """Removes background from an uploaded photo."""
    img = Image.open(input_path)
    output = remove(img)
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    output.save(out_path)
    return out_path


def compose_thumbnail(bg_path: str, cutout_path: str, text: str, out_path: str) -> str:
    """Overlay cutout and text onto background to create final thumbnail."""
    bg = Image.open(bg_path).convert("RGBA").resize((1280, 720))
    cutout = Image.open(cutout_path).convert("RGBA")
    cutout = cutout.resize((400, 400))
    bg.paste(cutout, (800, 200), cutout)
    draw = ImageDraw.Draw(bg)
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except Exception:
        font = ImageFont.load_default()
    draw.text((50, 600), text, font=font, fill="yellow", stroke_width=5, stroke_fill="black")
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    bg.save(out_path)
    return out_path
