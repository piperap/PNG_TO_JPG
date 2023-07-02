# PNG_TO_JPG
PNG to JPG Converter
This is a simple script to convert an image from PNG format to JPG format using Python's PIL (Pillow) library.

How to use
Make sure you have the Pillow library installed. If not, install it using pip:

Copy code
pip install pillow
To convert an image, simply replace 'input.png' and 'output.jpg' in the script with your input and output file names respectively.

Here is the Python script:

python
Copy code
from PIL import Image

img = Image.open('input.png')  # Open an image file.
rgb_im = img.convert('RGB')  # Convert the image to RGB mode.
rgb_im.save('output.jpg', 'JPEG')  # Save the converted image as a JPEG file.
Please note that converting from PNG (a lossless format) to JPG (a lossy format) may result in a decrease in image quality.
