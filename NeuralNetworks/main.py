#!/usr/bin/env python3

import os
import tensorflow as tf
import keras

from tensorflow.python.keras.initializers import glorot_uniform
from tensorflow.python.keras.models import (
    model_from_json,
    load_model
)
from tensorflow.keras.preprocessing.image import (
    load_img,
    img_to_array,
    array_to_img
)
from tensorflow.keras.utils import CustomObjectScope
from PIL import Image

def main():
    """
    Defining the path for the pre-trained models
    """
    MAIN_PATH = "models/"
    model = f"{MAIN_PATH}riceaiv4.json"
    weights = f"{MAIN_PATH}riceaiv4.hdf5"
    
    
    with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        with open(model, 'r') as f:
            model = model_from_json(f.read())
            model.load_weights(weights)
    
    image = Image.open("tests/rice_test2.jpeg")
    image = image.resize((224, 224))
    x = img_to_array(image) / 255.0
    x = x.reshape(1, 224, 224, 3)
    
    result = model.predict(x)
    print(result)


if __name__ == "__main__":
    main()
