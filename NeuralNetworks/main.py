#!/usr/bin/env python3

import os
import tensorflow as tf
import keras
from pwn import *
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
from typing import Any


def handle_image(path: str) -> Any:
    
    image = Image.open(f"tests/{path}")
    image = image.resize((224, 224))
    x = img_to_array(image) /255.0
    x = x.reshape(1, 224, 224, 3)
    return x


def accuracy_testing(path_model: int, 
                     path_image: str):
    """
    Defining the path for the pre-trained models
    """
    MAIN_PATH = "final_models/"
    # model = f"{MAIN_PATH}riceaiv{path_model}.json"
    # weights = f"{MAIN_PATH}riceaiv{path_model}.hdf5"
    
    model = f"{MAIN_PATH}final.{path_model}.json"
    weights = f"{MAIN_PATH}final.{path_model}.hdf5"
    
    log.progress(f"Loading model riceaiv{path_model} and loading {path_image}")
    
    with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
        with open(model, 'r') as f:
            model = model_from_json(f.read())
            model.load_weights(weights)
    
    x = handle_image(path_image)
    
    result = model.predict(x)
    
    
    print(result)
    
    
def main():
    try:
        accuracy_testing(2, "rice_test1.jpeg")
        accuracy_testing(2, "rice_test4.jpeg")
        
    except Exception as e:
        log.error("error in the testing models or json")
        print(str(e))


if __name__ == "__main__":
    main()
