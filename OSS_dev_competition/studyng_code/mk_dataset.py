import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator
import numpy as np
from PIL import Image

import matplotlib.pyplot as plt

Training_data_dir = "D:\CODES\data"

batch_size = 4


#Augmentation은 기존 이미지에 랜덤으로 변화를 주어서 
#적은사진이라도 여러 장 학습한것 처럼 하기 위한 기능이다.
training_data_Augmentation = ImageDataGenerator()
"""
training_data_Augmentation = ImageDataGenerator(
    rescale=1./255, #값범위를 0~1로 만들어 준다.
    rotation_range=0, #40도 각도 안에서 랜덤으로 회전
    width_shift_range=0, #좌우로 움직이는 정도
    height_shift_range=0, #상하로 움직이는 정도
    shear_range=0, #반전하는 정도
    zoom_range=0, #확대하는 정도
    brightness_range=(0,0), #랜덤하게 밝이 조정 앞에가 어두운정도, 뒤에가 밝은정도
    horizontal_flip=False, #좌우반전
    fill_mode='nearest', #이미지 변형에 따라 생기는 공백을 메우는 방식   
)
"""

#flow_from_directory 로 경로를 찾아가서 알아서
#딥러닝에 사용될 수 있는 형태로 변경해주는 작업
train_generator = training_data_Augmentation.flow_from_directory(
    Training_data_dir,
    batch_size=batch_size, #batch size 설정
    target_size=(50, 150), #픽셀값
    class_mode='categorical', #분류 방식에 대해 지정한다고 하는데 잘 모르겠음 
    shuffle=True #데이터 순서를 랜덤하게 가져온다.
)

img, label = next(train_generator)
r=g=b = 0

for i in range(4):
    image_name = img[i]
    im = Image.open(image_name)
    rgb_im = im.convert('RGB')
    r,g,b = rgb_im.getpixel((15, 17))
    print('R:'+ str(r) + ' G:' + str(g) + ' B:' + str(b))
