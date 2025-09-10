from rembg import remove
from PIL import Image

def cutout_photo(input_path: str, out_path="cutout.png"):
    """
    Removes background from an uploaded photo.
    """
    img = Image.open(input_path)
    output = remove(img)
    output.save(out_path)
    return out_path
