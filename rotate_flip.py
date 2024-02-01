from PIL import Image

# Load the image
image = Image.open("RAW.png")

# Rotate 90 degrees
rotated_90 = image.rotate(90)

# Rotate 180 degrees
rotated_180 = image.rotate(180)

# Horizontal flip
horizontal_flip = image.transpose(Image.FLIP_LEFT_RIGHT)

# Vertical flip
vertical_flip = image.transpose(Image.FLIP_TOP_BOTTOM)

# Display or save the rotated and flipped images
rotated_90.save("rotated_90.png")
# rotated_90.show()

rotated_180.save("rotated_180.png")
# rotated_180.show()

horizontal_flip.save("horizontal_flip.png")
# horizontal_flip.show()

vertical_flip.save("vertical_flip.png")
# vertical_flip.show()
