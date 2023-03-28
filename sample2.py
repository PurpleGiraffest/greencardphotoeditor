from PIL import Image
import streamlit as st
from rembg import remove


# Set the desired dimensions for the portrait image
new_width = 600
new_height = 600

# Set the path for the input and output files
input_file = "dvlottery/donnex.jpg"
output_file = "dvlottery/DVwithWaterMark.jpg"

# Open the input image file
with Image.open(input_file) as img:

    dpi = (300, 300)
    img.info['dpi'] = dpi
    # Resize the image to the desired dimensions
    img = img.resize((new_width, new_height))

    # Resize the image to the desired dimensions
    new_format = img.convert("RGB")
    img = remove(new_format)

    # Create a new image with a white background
    new_image = Image.new("RGBA", img.size, (255, 255, 255))

    # Paste the original image onto the new image, but without transparency
    new_image.paste(img, (0, 0), img)

    # Convert the image to JPEG format and save it
    new_image.convert("RGB").save(output_file, "JPEG")

    # Add watermark
    im1 = Image.open(output_file)
    im2 = Image.open('dvlottery/greencardlogo2.jpg')

    back_im = im1.copy()
    back_im.paste(im2, (70, 30))
    back_im.save(output_file, quality=95)


# Print a success message
print("Image successfully resized and converted to JPEG format!")

