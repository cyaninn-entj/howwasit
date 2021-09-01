import numpy as np
from PIL import Image
import glob
import re
import os

ls = glob.glob('data/top/*.jpg')
#factor=ls[0]
#print(factor)
# data/top\1.jpg

x1_data_R = [0]*len(ls)
x2_data_G = [0]*len(ls)
x3_data_B = [0]*len(ls)


for i, path in enumerate(ls) : 
    
    factor=path
    im = Image.open(factor)
    rgb_im = im.convert('RGB')

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

    x1_data_R[i] = r_AVG
    x2_data_G[i] = g_AVG
    x3_data_B[i] = b_AVG

print(x1_data_R)
print(len(x1_data_R))
#print('R:'+ str(r_AVG) + ' G:' + str(g_AVG) + ' B:' + str(b_AVG))

"""
(base) D:\CODES>C:/Anaconda/python.exe d:/CODES/main_ColorIs.py
[198.75, 124.125, 131.25, 112.125, 250.25, 43.625, 28.0, 71.125, 226.5, 202.875, 211.875, 38.0, 45.125, 243.75, 204.5, 198.0, 132.5, 86.125, 162.75, 99.125, 27.875, 217.25, 131.875, 213.25, 78.375, 30.5, 
41.125, 57.875, 235.75, 111.5, 180.5, 16.5, 143.5]
33
"""
