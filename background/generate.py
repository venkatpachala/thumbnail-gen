from diffusers import StableDiffusionPipeline
import torch

def generate_background(prompt: str, out_path="background.png"):
    """
    Generate a background image from text using Stable Diffusion (low-VRAM mode).
    """
    model_id = "runwayml/stable-diffusion-v1-5"

    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = pipe.to(device)

    # low-VRAM optimizations
    pipe.enable_attention_slicing()
    pipe.enable_sequential_cpu_offload()

    # smaller image size (fits T500 VRAM)
    image = pipe(prompt, height=512, width=512).images[0]
    image.save(out_path)
    return out_path
