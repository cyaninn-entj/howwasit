import numpy as np
from PIL import Image

im = Image.open('fitting_pic.jpg')
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((72, 49))

print(r, g, b)
