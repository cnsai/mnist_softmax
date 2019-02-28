import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

##### mnist 데이터셋 #####
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

##### 회귀 구현 #####
# x 데이터는 n개 * 784의 행렬로 구성되어 있다.
x = tf.placeholder(tf.float32, [None, 784])
# x와 행렬곱을 해줘야 하므로 x의 차원수인 784, 결과값은 10가지이다. 784*10 행렬. 
W = tf.Variable(tf.zeros([784, 10]))
# 결과 값(1*10)에 더해야 하므로 1*10
b = tf.Variable(tf.zeros([10]))
# softmax 함수를 적용하여 결과값을 0~1의 값으로 만든다.
# matmul : 행렬곱 함수
y = tf.nn.softmax(tf.matmul(x, W) + b)

##### 크로스 엔트로피 모델을 설정 #####
y_ = tf.placeholder(tf.float32, [None, 10])
c_e = -tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1])
# 크로스 엔트로피의 평균.
cross_entropy = tf.reduce_mean(c_e)

# 크로스 엔트로피 평균값이 작아지도록 경사하강법을 이용하여 최적화한다.
train_step = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cross_entropy)

##### 모델 평가 #####
# softmax 나온 값 중 가장 높은 값과 실제 데이터 비교해서 맞는지 체크
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
# 맞으면 1, 틀리면 0이므로 평균을 내면 정확도가 나온다.
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

##### 세션 그래프 생성 및 학습 시작 #####
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# 2000번 학습
for i in range(10000):
    # 학습 데이터셋에서 무작위 100개(batch)를 가져온다
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    if i % 100 == 0:
    #cost 값과 일치율을 같이 출력.
        loss, acc = sess.run([cross_entropy, accuracy], feed_dict={x: batch_xs, y_: batch_ys})
        print("Step : {:5}\tLoss: {:.3f}\tAcc: {:.2%}".format(i, loss, acc))


##### 정확도 출력 #####
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))