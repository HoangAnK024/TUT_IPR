from PIL import Image, ImageEnhance

def adjust_brightness(image, factor):
    """
    Adjust the brightness of the image.
    :param image: PIL Image object
    :param factor: Brightness factor (>1 to increase brightness, <1 to decrease brightness)
    :return: Adjusted PIL Image object
    """
    enhancer = ImageEnhance.Brightness(image)
    adjusted_image = enhancer.enhance(factor)
    return adjusted_image

def adjust_contrast(image, factor):
    """
    Adjust the contrast of the image.
    :param image: PIL Image object
    :param factor: Contrast factor (>1 to increase contrast, <1 to decrease contrast)
    :return: Adjusted PIL Image object
    """
    enhancer = ImageEnhance.Contrast(image)
    adjusted_image = enhancer.enhance(factor)
    return adjusted_image

# Load the image
image = Image.open("RAW.png")

# Adjust brightness (increase by a factor of 1.5)
brightened_image = adjust_brightness(image, 1.5)

# Adjust contrast (increase by a factor of 1.5)
high_contrast_image = adjust_contrast(image, 1.5)

# Display or save the adjusted images
brightened_image.save("brightened_image.png")
# brightened_image.show()

high_contrast_image.save("high_contrast_image.png")
# high_contrast_image.show()
