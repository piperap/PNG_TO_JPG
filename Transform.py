from PIL import Image

img = Image.open('/Users/felipeojeda/Desktop/Proyectos/yumisite.com/weberpaxPro/APP/myapp/public/assets/templates/01a/profile.png')
rgb_im = img.convert('RGB')
rgb_im.save('/Users/felipeojeda/Desktop/Proyectos/yumisite.com/weberpaxPro/APP/myapp/public/assets/templates/01a/profile.jpg', 'JPEG')