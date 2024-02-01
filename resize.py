from PIL import Image

def resize_image(input_path, output_path, new_width, new_height) :
    # Load img
    image = Image.open(input_path)

    # Resize img
    resized_img = image.resize((new_width, new_height))

    # Save img
    resized_img.save(output_path)

    print(f"Resize image saved as {output_path}")

resize_image("RAW.png","resized_image.png", 800, 600)