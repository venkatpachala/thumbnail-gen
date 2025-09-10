from PIL import Image, ImageDraw, ImageFont

def compose_thumbnail(bg_path: str, cutout_path: str, text: str, out_path="thumbnail.png"):
    """
    Overlay cutout and text onto background to create final thumbnail.
    """
    bg = Image.open(bg_path).convert("RGBA").resize((1280, 720))
    cutout = Image.open(cutout_path).convert("RGBA")

    # resize cutout
    cutout = cutout.resize((400, 400))
    bg.paste(cutout, (800, 200), cutout)

    # add text
    draw = ImageDraw.Draw(bg)
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except:
        font = ImageFont.load_default()

    draw.text((50, 600), text, font=font, fill="yellow", stroke_width=5, stroke_fill="black")

    bg.save(out_path)
    return out_path
