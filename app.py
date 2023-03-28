from pathlib import Path

import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "photo_size.jpg"
profile_pic = current_dir / "photo_size.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Photo | Visa"
PAGE_ICON = ":wave:"
NAME = "Visa Photo Generator based on Requirements"
DESCRIPTION = """
Visa Photo Generator based on Requirements
"""

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" \
integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
            unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color:#e9f2f4;">
  <a class="navbar-brand" href="" target="_blank"><img src="https://greencardphotoeditor.com/greencard_logo.png" style="width:100px;height:100px;"></a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="" target="_blank">Visa Requirements</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="" target="_blank">Contacts</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
st.header('Passport or Visa Photo in 2 Seconds')

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)

st.write("## Remove background from your image")
st.write(
    "Take an image with a smartphone or camera against any background, upload it here and instantly get a professional photo for your visa, passport or ID."
)
st.write("## Upload and download :gear:")


# Set the desired dimensions for the portrait image
new_width = 600
new_height = 600

# Set the path for the input and output files
# input_file = "dvlottery/donnex.jpg"
output_file = "dvlottery/images/maintest.jpg"

def fix_image(upload):
    img = Image.open(upload)

    col1.write("Original Image :camera:")
    col1.image(img)

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

    col2.write("Fixed Image :wrench:")
    col2.image(back_im)
    st.markdown("\n")
    st.download_button("Download fixed image", "maintest", "image/jpg")
    # convert_image(fixed),



    #To remove the watermark when the payment is made, you can simply
    # delete the watermarked image. Then, you can provide a download link
    # to the original image without the watermark. For example:


# Delete the watermarked image
#os.remove("watermarked_image.png")

# Provide a download link to the original image
#download_link = "https://example.com/original_image.png"


col1, col2 = st.columns(2)
my_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("./dvlottery/donnex.jpg")

# Removes the nav bar top padding
st.write('<style>div.block-container{padding-top:4.0rem;}</style>', unsafe_allow_html=True)

st.write("Important Notice: The selection process for the DV lottery is the sole responsibility of the US Government. "
         "Using the Greencard Photo Editor website does not guarantee success in the DV lottery application process."
         " While our website uses AI technology to ensure that photos meet the DV lottery photo requirements, "
         "the selection process is determined solely by the US Government. We provide this service solely to assist applicants "
         "in meeting the photo requirements. We do not guarantee that your application will be accepted, nor do we have any control"
         " over the outcome of the selection process."
         " For more information about the DV lottery selection process, please visit the official website of the US Department of State.")