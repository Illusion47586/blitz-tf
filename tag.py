import pickle
import numpy as np
from PIL import ImageFile
from keras.applications.densenet import DenseNet121, preprocess_input
from keras.models import Model, load_model
from keras.preprocessing import image
from keras.preprocessing.sequence import pad_sequences

ImageFile.LOAD_TRUNCATED_IMAGES = True

model = load_model('./saved/model_15.h5')
model.make_predict_function()

model_temp = DenseNet121(weights='imagenet', input_shape=(224, 224, 3))

model_dense = Model(model_temp.input, model_temp.layers[-2].output)

model_dense.make_predict_function()

with open("./saved/word_to_idx.pkl", 'rb') as w2i:
    word_to_idx = pickle.load(w2i)

with open("./saved/idx_to_word.pkl", 'rb') as i2w:
    idx_to_word = pickle.load(i2w)


def preprocess_image(img):
    img = image.load_img(img, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img


def encode_image(img):
    img = preprocess_image(img)
    feature_vector = model_dense.predict(img)
    feature_vector = feature_vector.reshape(1, feature_vector.shape[1])
    return feature_vector


def predict_caption(photo):
    in_text = "startseq"
    max_len = 5
    for i in range(max_len):
        sequence = [word_to_idx[w]
                    for w in in_text.split() if w in word_to_idx]
        sequence = pad_sequences([sequence], maxlen=max_len, padding='post')
        ypred = model.predict([photo, sequence])
        ypred = ypred.argmax()
        word = idx_to_word[ypred]
        in_text += ' ' + word

        if word == 'endseq':
            break

    final_caption = in_text.split()
    final_caption = final_caption[1:-1]
    final_caption = ' '.join(final_caption)

    return final_caption


def getTag(path: str) -> object:
    enc = encode_image(path)
    tags = predict_caption(enc)
    return tags


# print(getTag("./test.png"))
