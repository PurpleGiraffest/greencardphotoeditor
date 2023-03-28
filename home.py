from PIL import Image
import streamlit as st
from rembg import remove


# Set the desired dimensions for the portrait image
new_width = 600
new_height = 600

# Set the path for the input and output files
input_file = "dvlottery/donnex.jpg"
output_file = "dvlottery/KO5.jpg"

# Open the input image file
with Image.open(input_file) as img:

    img.save('donnex.png')
    # Resize the image to the desired dimensions
    img = img.resize((new_width, new_height))

    # Remove image background
    fixed = remove(img)

    # Create a new image with a white background
    new_image = Image.new("RGBA", img.size, (245, 189, 165))

    # Paste the original image onto the new image, but without transparency
    new_image.paste(fixed, (0, 0), img)

    # Convert the image to JPEG format and save it
    new_image.convert("RGB").save(output_file, "JPEG")

    # Save the output image file
    # img.save(output_file, "JPEG")

# Print a success message
print("Image successfully resized and converted to JPEG format!")


