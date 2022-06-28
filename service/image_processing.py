from service.utilities import decode_raw_image, get_array_image, get_fileinfo
import cv2

def image_process(raw_image):
    decoded_bytes = decode_raw_image(raw_image)
    array_image = get_array_image(decoded_bytes)

    processed_image = _processing(array_image)

    file_info = get_fileinfo(processed_image)

    return file_info


def _processing(array_image):
    array_image = cv2.cvtColor(array_image, cv2.COLOR_BGR2GRAY)
    _, array_image = cv2.threshold(array_image,0,255,cv2.THRESH_OTSU)
    return array_image
