import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow import keras


# define paths

TRAIN_DIR = '/Users/jihoon/venvs/modu_deep/datasets/70dog_breeds_image_dataset/train'

DIMS = (224,224)
IMG_SIZE = 224
BATCH_SIZE = 32
SEED = 42

data_gen = ImageDataGenerator(rescale=1/255)

train_data = data_gen.flow_from_directory(batch_size=BATCH_SIZE,
                                         directory=TRAIN_DIR,
                                         shuffle=True,
                                         target_size=DIMS,
                                         class_mode='categorical')

label_mapper = np.asarray(list(train_data.class_indices.keys()))


def classify_dog_breed(img_path):
    img = load_img(img_path, target_size=DIMS)
    model = keras.models.load_model("/Users/jihoon/venvs/modu_deep/model/CNN_InceptionV3/08-0.9711.h5")
    # display(img)
    arr = img_to_array(img)
    arr = arr/255.0
    arr = np.expand_dims(arr,0)
    res = model.predict(arr)
    print(res.shape)
    idx = res.argmax()
    return label_mapper[idx], res[0][idx]