import numpy as np
from PIL import Image
import glob
import re
import os

ls = glob.glob('data/top/*.jpg')

#print(ls)
# ['temp/[x].txt', 'temp/1.txt', 'temp/123.txt']

#print(type(ls))
# <class 'list'>

factor=ls[0]
print(factor)
# data/top\1.jpg

im = Image.open(factor)
rgb_im = im.convert('RGB')

r_list = []
g_list = []
b_list = []

r_list = [0]*8
g_list = [0]*8
b_list = [0]*8

r_list[0], g_list[0], b_list[0] = rgb_im.getpixel((15, 17))
r_list[1], g_list[1], b_list[1] = rgb_im.getpixel((35, 17))
r_list[2], g_list[2], b_list[2] = rgb_im.getpixel((15, 30))
r_list[3], g_list[3], b_list[3] = rgb_im.getpixel((35, 30))
r_list[4], g_list[4], b_list[4] = rgb_im.getpixel((15, 45))
r_list[5], g_list[5], b_list[5] = rgb_im.getpixel((35, 45))
r_list[6], g_list[6], b_list[6] = rgb_im.getpixel((15, 60))
r_list[7], g_list[7], b_list[7] = rgb_im.getpixel((35, 60))

r_AVG = sum(r_list, 0.0) / len(r_list)
g_AVG = sum(g_list, 0.0) / len(g_list)
b_AVG = sum(b_list, 0.0) / len(b_list)

print('R:'+ str(r_AVG) + ' G:' + str(g_AVG) + ' B:' + str(b_AVG))
