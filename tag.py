import pickle
import numpy as np
import os
from PIL import ImageFile
import keras
from keras.applications.densenet import DenseNet121, preprocess_input
from keras.models import Model, load_model
from keras.preprocessing import image
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

ImageFile.LOAD_TRUNCATED_IMAGES = True

models = {}
encoders = {}
Class = []
for file in os.listdir('saved/model'):
    print(file)
    ClassName = file.split('.')[0].split('_')[1]
    Class.append(ClassName)
    models[ClassName] = keras.models.load_model('saved/model/' + file)

for file in os.listdir('saved/encoder'):
    print(file)
    ClassName = file.split('.')[0].split('_')[0]
    encoder = LabelEncoder()
    encoder.classes_ = np.load('saved/encoder/' + file, allow_pickle=True)
    encoders[ClassName] = encoder

model_temp = DenseNet121(weights='imagenet', input_shape=(224, 224, 3))
model_dense = Model(model_temp.input, model_temp.layers[-2].output)
model_dense.make_predict_function()


def preprocess_image(img):
    img = image.load_img(img, target_size=(224, 224))
    img = np.array([image.img_to_array(img)])
    return img


def encode_image(img):
    img = preprocess_image(img)
    feature_vector = model_dense.predict(img)
    feature_vector = feature_vector.reshape(1, feature_vector.shape[1])
    return feature_vector


def predict_caption(photo):
    final_caption = {}
    for Cl in Class:
        Y_pred = models[Cl].predict(photo)
        Y_label = encoders[Cl].inverse_transform([np.argmax(Y_pred)])
        final_caption[Cl] = Y_label[0]

    return final_caption


def getTag(path: str) -> object:
    enc = encode_image(path)
    tags = predict_caption(enc)
    return tags

# print(getTag("./test.png"))

