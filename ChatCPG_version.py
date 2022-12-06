# Import the required modules
import os
from PIL import Image

# Define the input value
unit_number = input("Enter your unit number")

# Create an empty list to store the images
images = []

# Loop through each digit in the input value
for digit in str(unit_number):
    # Load the image from the file
    image = Image.open(f"{digit}.jpg")
    # Add the image to the list
    images.append(image)

# Create a new image that is the width of all the images combined
result_image = Image.new("RGB", (sum([img.width for img in images]), images[0].height))

# Paste the images into the new image, one after the other
x_offset = 0
for img in images:
    result_image.paste(img, (x_offset, 0))
    x_offset += img.width

# Save the final result
result_image.save("str(unit_number).jpg")