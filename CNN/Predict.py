
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras.layers.core import Dropout
from keras.models import Sequential 


input_shape = (224,224,3)
img_width, img_height = 64,64
batch_size = 30
samples_per_epoch = 240
validation_steps = 32
nb_filters1 = 32
nb_filters2 = 64
conv1_size = 3
conv2_size = 3
pool_size = 2
classes_num = 2
lr = 0.0001


model = Sequential()
model.add(Conv2D(nb_filters1,(conv1_size, conv1_size), padding ="same",input_shape=(img_width, img_height, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(pool_size, pool_size)))
model.add(Conv2D(nb_filters2, (conv2_size, conv2_size), padding ="same"))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(pool_size, pool_size), dim_ordering='th'))
model.add(Flatten())
model.add(Dense(256))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(classes_num, activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer=optimizers.Adam(lr=lr, beta_1=0.9,beta_2=0.999, epsilon=None, decay=0.0),metrics=['accuracy'])
model.load_weights('CNN/models/weights.h5')
