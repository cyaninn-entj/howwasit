import numpy as np
import pandas as pd
from PIL import Image
import glob
import re
import os

ls = glob.glob('data/top/*.jpg')
#디렉토리 리스트로 가져오기
'''
#factor=ls[0]
#print(factor)
# data/top\1.jpg
'''

index=["color", "color_name", "hex", "R", "G", "B", "number"]
csv = pd.read_csv('colors_yw.csv', names=index, header=None)
#csv 리스트로 명명해주기, csv 파일 불러오기

x1_data_R = [0]*len(ls)
x2_data_G = [0]*len(ls)
x3_data_B = [0]*len(ls)
Y_data = [0]*len(ls)
#데이터 담는 리스트 공간 설정

for i, path in enumerate(ls) : 
    
    factor=path
    im = Image.open(factor)
    rgb_im = im.convert('RGB')
    #이미지 불러오기

    r_list = [0]*8
    g_list = [0]*8
    b_list = [0]*8
    #rgb 평균을 담을 리스트 생성

    r_list[0], g_list[0], b_list[0] = rgb_im.getpixel((15, 17))
    r_list[1], g_list[1], b_list[1] = rgb_im.getpixel((35, 17))
    r_list[2], g_list[2], b_list[2] = rgb_im.getpixel((15, 30))
    r_list[3], g_list[3], b_list[3] = rgb_im.getpixel((35, 30))
    r_list[4], g_list[4], b_list[4] = rgb_im.getpixel((15, 45))
    r_list[5], g_list[5], b_list[5] = rgb_im.getpixel((35, 45))
    r_list[6], g_list[6], b_list[6] = rgb_im.getpixel((15, 60))
    r_list[7], g_list[7], b_list[7] = rgb_im.getpixel((35, 60))
    #상의 8개 좌표 rgb 추출

    r_AVG = sum(r_list, 0.0) / len(r_list)
    g_AVG = sum(g_list, 0.0) / len(g_list)
    b_AVG = sum(b_list, 0.0) / len(b_list)
    #8개의 rgb 값의 각각 평균

    x1_data_R[i] = r_AVG
    x2_data_G[i] = g_AVG
    x3_data_B[i] = b_AVG
    #데이터 리스트에 평균값 담기

    r_list[0], g_list[0], b_list[0] = rgb_im.getpixel((15, 90))
    r_list[1], g_list[1], b_list[1] = rgb_im.getpixel((35, 90))
    r_list[2], g_list[2], b_list[2] = rgb_im.getpixel((15, 105))
    r_list[3], g_list[3], b_list[3] = rgb_im.getpixel((35, 105))
    r_list[4], g_list[4], b_list[4] = rgb_im.getpixel((15, 120))
    r_list[5], g_list[5], b_list[5] = rgb_im.getpixel((35, 120))
    #하의 6개좌표 rgb 추출

    r_AVG = sum(r_list, 0.0) / len(r_list)
    g_AVG = sum(g_list, 0.0) / len(g_list)
    b_AVG = sum(b_list, 0.0) / len(b_list)
    #6개의 rgb 값의 각각 평균

    minimum = 10000
    for j in range(len(csv)):
        d = abs(r_AVG- int(csv.loc[j,"R"])) + abs(g_AVG- int(csv.loc[j,"G"]))+ abs(b_AVG- int(csv.loc[j,"B"]))
        if(d<=minimum):
            minimum = d
            Y_color_num = csv.loc[j,"number"]
    #구해낸 rgb 값에 대응하는 csv 파일 내의 일련번호 찾기
    
    Y_data[i] = Y_color_num
    #일련번호를 데이터 리스트에 저장



print("x1data_0: "+str(x1_data_R[0])+" x2data_0: "+str(x2_data_G[0])+" x3data_0 :"+str(x3_data_B[0])+" Y_data_0 :"+str(Y_data[0]))
print("x1 data len: "+ str(len(x1_data_R)))
print("x2 data len: "+ str(len(x2_data_G)))
print("x3 data len: "+ str(len(x3_data_B)))
print("y data len: "+ str(len(Y_data)))
#print('R:'+ str(r_AVG) + ' G:' + str(g_AVG) + ' B:' + str(b_AVG))
