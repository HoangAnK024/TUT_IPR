from PIL import Image

def convert_to_grayscale(image_path, output_path):
    # Load the image
    image = Image.open(image_path)

    #convert to grayscale
    grayscale_image = image.convert('L')

    # Save the grayscale image
    grayscale_image.save(output_path)

    print(f"Grayscale image saved as {output_path}")

convert_to_grayscale("RAW.png", "grayscale_image.png")