import base64
from io import BytesIO

import cv2
import numpy as np
from PIL import Image


def create_response(success, data, error=""):
    content = {
        'success': success,
        'data': data,
        'error': error
    }
    return content


def decode_raw_image(raw_image):
    decoded_bytes = base64.b64decode(raw_image)
    return decoded_bytes


def get_array_image(decoded_bytes):
    bytes_raw = BytesIO(decoded_bytes)
    source = Image.open(bytes_raw)
    array_image = np.array(source)
    return array_image


def get_fileinfo(processed_image):
    success, compress_image = cv2.imencode('.jpeg', processed_image)
    encoded_image = base64.b64encode(compress_image).decode("utf8")
    width = processed_image.shape[0]
    height = processed_image.shape[1]
    file_info = {
        'width': width,
        'height': height,
        'content': encoded_image
    }
    return file_info
