# import cv2
# # LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread("RAW.png")
# # DISPLAY
# cv2.imshow("Result", img)
# cv2.waitKey(0) 

from PIL import Image
import matplotlib.pyplot as plt

def load_and_display_image(image_path):
    # Load the image
    image = Image.open(image_path)
    # image.show()


    # Display the image
    plt.imshow(image)
    plt.axis('off')
    plt.show()


load_and_display_image("RAW.png")


