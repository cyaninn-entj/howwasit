import numpy as np
from PIL import Image

im = Image.open('1.jpg')
rgb_im = im.convert('RGB')

r_list = []
g_list = []
b_list = []

r_list = [0]*10
g_list = [0]*10
b_list = [0]*10

r_list[0], g_list[0], b_list[0] = rgb_im.getpixel((4, 11))
r_list[1], g_list[1], b_list[1] = rgb_im.getpixel((16, 17))
r_list[2], g_list[2], b_list[2] = rgb_im.getpixel((32, 8))
r_list[3], g_list[3], b_list[3] = rgb_im.getpixel((42, 8))
r_list[4], g_list[4], b_list[4] = rgb_im.getpixel((17, 24))
r_list[5], g_list[5], b_list[5] = rgb_im.getpixel((32, 24))
r_list[6], g_list[6], b_list[6] = rgb_im.getpixel((17, 34))
r_list[7], g_list[7], b_list[7] = rgb_im.getpixel((32, 34))

r_AVG = sum(r_list, 0.0) / len(r_list)
g_AVG = sum(g_list, 0.0) / len(g_list)
b_AVG = sum(b_list, 0.0) / len(b_list)

print('R:'+ str(r_AVG) + ' G:' + str(g_AVG) + ' B:' + str(b_AVG))
