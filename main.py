import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import ds as ma
import numpy as np

## Hyperparameters
batch_size = 128
num_classes = 10
epochs = 50

## Load Datasets
x_a = ma.train_x
y_a = keras.utils.to_categorical(ma.train_y, num_classes)

img_rows, img_cols = 28, 28

(x_train, y_train), (x_test, y_test) = mnist.load_data()

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

print(y_test[0])
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
print(y_test[0])

# Convnet
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='elu', input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='elu'))
model.add(Conv2D(128, (5, 5), activation='elu'))
model.add(Conv2D(256, (5, 5), activation='elu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation='elu'))
model.add(Dense(128, activation='elu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

print(x_train.shape, y_train.shape)
x_train = np.concatenate((x_train, x_a, x_test), axis = 0)
y_train = np.concatenate((y_train, y_a, y_test), axis = 0)

def fit():
    ### Gradient Descent
    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_split = 0.05)

def sc():
    return model.predict(ma.test_x)

fit()
y = sc()
