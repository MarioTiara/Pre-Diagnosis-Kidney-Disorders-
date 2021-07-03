from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import numpy as np
model_path = 'D:/LCD/CNN/models/model.h5'
model_weights_path = 'D:/LCD/CNN/models/weights.h5'
model = load_model(model_path)
print(model.summary)
model.load_weights(model_weights_path)
IMG_SIZE=(150,150)
file='D:/LCD/CNN/data/data_recognition/Kiri/ginjal/HasilKondisi.jpg'
x = load_img(file, target_size=IMG_SIZE)
x = img_to_array(x)
x = np.expand_dims(x, axis=0)
print(x)
Result=model.predict(x)
print(Result)
print("Done")
