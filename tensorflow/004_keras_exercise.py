from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# opens an image using PIL
# resize it
# show numpy array details

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print("train_images.shape, test_images.shape", train_images.shape, test_images.shape)
print("train_images axes, test_images axes, .dtype", train_images.ndim, test_images.ndim, train_images.dtype)

# show an image from test_images
img_index = 0
digit = test_images[img_index]
print(digit.shape)
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()

# prints the matrix from the test_image
for row in test_images[img_index]:
    print row

file_name = "pics/1_1"
img = Image.open(file_name+'.png')
plt.imshow(img, cmap=plt.cm.binary)
plt.show()

data = np.array(img, dtype='uint8' )
print(data.shape)

# print(10*data)


