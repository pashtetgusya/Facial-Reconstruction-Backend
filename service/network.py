from service.utilities import decode_raw_image, get_array_image, get_fileinfo

from keras_contrib.layers.normalization.instancenormalization import InstanceNormalization
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from keras.models import load_model
import numpy as np
import cv2

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

def network_process(model, raw_image):
    decoded_bytes = decode_raw_image(raw_image)
    array_image = get_array_image(decoded_bytes)

    processed_image = _processing(model, array_image)

    file_info = get_fileinfo(processed_image)

    return file_info


def _processing(model, array_image):
    array_image = cv2.cvtColor(array_image, cv2.COLOR_BGR2RGB)
    array_image = cv2.resize(array_image, (256, 256))
    norm_img = (array_image.copy() - 127.5) / 127.5

    generated_image = model.predict(np.expand_dims(norm_img, 0))[0]
    generated_image = generated_image * 127.5 + 127.5
    
    generated_image = cv2.cvtColor(generated_image, cv2.COLOR_BGR2RGB)
    generated_image = cv2.resize(generated_image, (200, 250))
    return generated_image


def get_model():
    
    # инициализация модели
    g_loaded_model = load_model(
        '/Users/agella/work/md/painting_service/service/points/g_model.h5',
        custom_objects={'InstanceNormalization':InstanceNormalization}, 
        compile = False
    )
    return g_loaded_model
