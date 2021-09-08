from typing_extensions import Annotated
import numpy as np
import pandas as pd
from PIL import Image
import glob
import re
import os
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

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

x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
#placeholder로 저장

w1 = tf.Variable(tf.random_normal([1]), name = 'weight1')
w2 = tf.Variable(tf.random_normal([1]), name = 'weight2')
w3 = tf.Variable(tf.random_normal([1]), name = 'weight3')
b = tf.Variable(tf.random_normal([1]),name = 'bias')
#구하려는 국어,수학,영어 점수

hypothesis = x1 * w1 + x2 * w2 + x3 * w3 + b
#Hypothesis(y추정값) = w1*x1 + w2*x2 + w3*x3 + b

cost = tf.reduce_mean(tf.square(hypothesis - Y)) 
#추정한 값(Hypothesis)와 실제값(y)의 차이를 제곱하여 수식을 만드는 부분

optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)
#Cost(비용)을 아래로 볼록한 2차함수로 만들고, 미분했을때 0인 지점의 W와 b값이 이상적인 결과
#이 과정을 텐서플로우가 함수형식으로 만들어서 그냥 제공해주는 부분

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for step in range(10001) : 
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
    feed_dict = { x1 : x1_data_R, x2 : x2_data_G, x3 : x3_data_B, Y : Y_data})
    if step % 2000 == 0 :
        print(step, "Cost : ",cost_val,"\nPrediction:\n",hy_val, 
        "\nWeight,bias :\n",sess.run(w1),sess.run(w2),sess.run(w3),sess.run(b))
        print("==============")


w1_result = sess.run(w1)
w2_result = sess.run(w2)
w3_result = sess.run(w3)
b_result = sess.run(b)
for k in range(len(csv)):
    answer = int(csv.loc[k,"R"]) * w1_result + int(csv.loc[k,"G"]) * w2_result + int(csv.loc[k,"B"]) * w3_result + b_result
    print("입력상의 색: "+str(csv.loc[k,"number"]))
    print("하의 색 : "+str(answer))
    print("============")
