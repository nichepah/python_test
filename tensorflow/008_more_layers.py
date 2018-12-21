from keras import models
from keras import layers

from keras.datasets import mnist
from keras.utils import to_categorical

import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print("train_images.shape, test_images.shape", train_images.shape, test_images.shape)
print("train_images axes, test_images axes, train_images.dtype", train_images.ndim, test_images.ndim, train_images.dtype)

network = models.Sequential()

# adds layers
# choice of layer is related to the problem in hand
# relu is Rectified Linear Units
# 512 hidden layers
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
# network.add(Dropout(0.2))
network.add(layers.Dense(512, activation='relu'))
# softmax, returns an array of 10 probablity scores, corresponding to the counting numbers
network.add(layers.Dense(10, activation='softmax'))
network.summary()

# for training provide 3 parameters
# loss function, optimizer, and metrics
network.compile(optimizer='rmsprop',
                          loss='categorical_crossentropy',
                          metrics=['accuracy'])

# reshape the matrices to a shape that the network expects
# original train_images is of shape (6000, 28, 28) of type unit8
# of values [0, 255]
# transform it to float32 of (60000, 28*28)
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

# similarly for test_images
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# categorically encode the labels
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# train the network with fit method
network.fit(train_images, train_labels, epochs=5, batch_size=128)
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_accuracy:', test_acc)

network.save('csi_training_handwritten_3_layers.h5')

# on training data : loss: 0.0287 - acc: 0.9910
# ('test_accuracy:', 0.9788)
# compare it against results of 001: train, test accuracies were (0.9886 and 0.981)

