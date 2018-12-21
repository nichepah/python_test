from keras import models
from keras import layers

from keras.datasets import mnist
from keras.utils import to_categorical

import matplotlib.pyplot as plt

# generally data can be of 4 types
# 1. Vector data: 2D tensors of shape (samples, features)
# 2. Timeseries data : 3D tensors of shape (samples, timesteps,
#    and features)
# 3. Images: 4D tensors of shape (samples, height, width,
#    channels) or (samples,channels, height, width)
# 4. Video: 5D tensors of shape (samples, frames, height,
#    width, channels) or (samples, frames, channels, height, width)

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print("train_images.shape, test_images.shape", train_images.shape, test_images.shape)
print("train_images axes, test_images axes, train_images.dtype", train_images.ndim, test_images.ndim, train_images.dtype)

# show an image
img_index = 123
digit = test_images[img_index]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()

network = models.Sequential()

# adds layers
# choice of layer is related to the problem in hand
# relu is Rectified Linear Units
# 512 hidden layers
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))

# softmax, returns an array of 10 probablity scores, corresponding to the
# counting numbers
network.add(layers.Dense(10, activation='softmax'))

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

network.save('csi_training_handwritten.h5')

# convert to json
network_json = network.to_json()
with open("csi_training_handwritten.json", "w") as json_file:
    json_file.write(network_json)

# convert to yaml
network_yaml = network.to_yaml()
with open("csi_training_handwritten.yaml", "w") as yaml_file:
    yaml_file.write(network_yaml)

# training set: 3s 43us/step - loss: 0.0373 - acc: 0.9886
# ('test_accuracy:', 0.981)
