from background.generate import generate_background
from photo.cutout import cutout_photo
from compose.compose import compose_thumbnail

def main():
    prompt = "Cooking thumbnail with biryani pot and fire effects"
    user_photo = "your_photo.jpg"

    # Step 2: Generate background
    bg_path = generate_background(prompt)

    # Step 3: Cutout user photo
    cutout_path = cutout_photo(user_photo)

    # Step 4: Compose final thumbnail
    final_path = compose_thumbnail(bg_path, cutout_path, "BEST BIRYANI RECIPE!")
    print(f"✅ Thumbnail created: {final_path}")

if __name__ == "__main__":
    main()
