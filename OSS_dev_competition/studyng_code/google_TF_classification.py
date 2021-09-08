import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
#TensorFlow 및 기타 라이브러리 가져오기

import pathlib
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file('flower_photos', origin=dataset_url, untar=True)
data_dir = pathlib.Path(data_dir)
#데이터세트 다운로드 및 탐색하기
#이 튜토리얼에서는 약 3,700장의 꽃 사진 데이터세트를 사용합니다. 데이터세트에는 클래스당 하나씩 5개의 하위 디렉토리가 있습니다.
"""
dataset_url 에서 링크로 압축파일을 받고
압출을 해제하는 작업을 한 뒤
pathlib.Path 로 경로를 저장해준다.
"""

image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)
#다운로드 후, 데이터세트 사본을 사용할 수 있습니다. 총 3,670개의 이미지가 있습니다.
"""
glob()은 많은 파일을 다룰때 사용자가 제시한 조건에 맞는 
파일명을 리스트 형식으로 반환해준다.
'*'은 임의 길이의 모든 문자열을 의미하고
'?'는 한자리 문자를 의미한다.
위 코드라면 .jpg로 끝나고 '문자열/문자열'형태의 파일을 리스트 형식으로 반환해
그 리스트의 길이(인수의 개수)를 출력하는 코드인듯
"""

roses = list(data_dir.glob('roses/*'))
PIL.Image.open(str(roses[0]))
PIL.Image.open(str(roses[1]))

tulips = list(data_dir.glob('tulips/*'))
PIL.Image.open(str(tulips[0]))
PIL.Image.open(str(tulips[1]))

batch_size = 32
img_height = 180
img_width = 180
#로더에 대한 몇 가지 매개변수를 정의합니다.

#모델을 개발할 때 검증 분할을 사용하는 것이 좋습니다. 훈련에 이미지의 80%를 사용하고 검증에 20%를 사용합니다.
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)
#훈련 데이터셋

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)
#검증 데이터셋

class_names = train_ds.class_names
print(class_names)
