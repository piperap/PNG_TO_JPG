from PIL import Image

img = Image.open('profile.png')
rgb_im = img.convert('RGB')
rgb_im.save('profile.jpg', 'JPEG')
