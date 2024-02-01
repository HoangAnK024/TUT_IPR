from PIL import Image

# Load the image
image = Image.open("RAW.png")

# Specify the coordinates of the portion you want to crop
left = 100
top = 100
right = 400
bottom = 400

# Crop the specified portion
cropped_image = image.crop((left, top, right, bottom))

# Save or display the cropped image
cropped_image.save("cropped_image.png")
# cropped_image.show()
