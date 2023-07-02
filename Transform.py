from PIL import Image

img = Image.open('input.png')
rgb_im = img.convert('RGB')
rgb_im.save('output.jpg', 'JPEG')