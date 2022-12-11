import re
from PIL import Image
import base64


def summary(s):
    return re.sub(r'дождь', replacer, s)


def replacer(match):
    return 'снег'


def generate_img(image_path):
    img = Image.new('RGB', (200, 200), 'black')
    img.save(image_path)


def encode_image(image_path):
    with open(image_path, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64decode(binary_file_data)
        base64_message = base64_encoded_data.decode('unicode_escape')

        return base64_message
