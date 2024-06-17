#!/usr/bin/env python3

# The module will create a general QR Code
# to create the QR code can be found

# The qrcode module can be installed with: pip install qrcode
import qrcode
from qrcode.image.pure import PyPNGImage
import sys

# You need pillow module for image processing
# https://pypi.org/project/pillow/
# Install with: pip install pillow

#import image processing modules
from PIL import Image, ImageDraw, ImageFont

# Check command line arguments. If an argument is set use it instead of the defaults below. 
# The arguments need to be in order
# Script Weblink Text File

# Set your variables. They are all in one spot to make it easier. If tehre are no command line
# variables these are the defautls
Weblink = "https://amazon.com"
Imgtext = "Amazon.com"
imgfile = "Amazon_QR_Link.png"

if len(sys.argv) > 1:
    Weblink = sys.argv[1]
if len(sys.argv) > 2:
    Imgtext = sys.argv[2]
if len(sys.argv) > 3:
    imgfile = sys.argv[3]
 

# Generate the basic QRCode

img = qrcode.make(Weblink, image_factory=PyPNGImage)

# Save the image. This is just temporary
img.save("Tmpimg.png")

#Now we need to adjust the QRCode image

# Open the image so we can add text below
simg = Image.open("Tmpimg.png")

# Define the desired extra space below the QR Code (e.g., 100 pixels)
extra_space_height = 50

# Create a new image with white background
new_height = simg.height + extra_space_height
new_img = Image.new('RGB', (simg.width, new_height), color='white')

# Paste the original image at the top
new_img.paste(simg, (0, 0))

# Create a drawing object
draw = ImageDraw.Draw(new_img)

# Load a font 
# Using basic courier font for the text under the QRCode
myFont = ImageFont.truetype('\windows\fonts\cour.ttf', 30)

# Add text with the defined font style
# Put the text at 90 pixels from the bottom of the image. Color is black.
draw.text((30, (new_img.height - 90)), Imgtext, font=myFont, fill=(0,0,0))

# Save the modified final image to the specified file
new_img.save(imgfile)

# Optionally, display the modified image
new_img.show()
