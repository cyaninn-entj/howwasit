import tensorflow.compat.v1 as tf
import numpy as np
tf.disable_v2_behavior()


x1_data = [73., 93., 89., 96., 73.] #국어점수
x2_data = [80., 88., 91., 98., 66.] #수학점수
x3_data = [75., 93., 90., 100., 70.] #영어점수
y_data = [152., 185., 180., 196., 142.] #최종스코어

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

for step in range(2001) : 
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train],
    feed_dict = { x1 : x1_data, x2 : x2_data, x3 : x3_data, Y : y_data})
    if step % 1000 == 0 :
        print(step, "Cost : ",cost_val,"\nPrediction:\n",hy_val, 
        "\nWeight,bias :\n",sess.run(w1),sess.run(w2),sess.run(w3),sess.run(b))
