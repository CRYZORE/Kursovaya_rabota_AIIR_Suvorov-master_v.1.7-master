from django.db import models
import base64

from summary.sum.func import summary
from summary.sum.func import generate_img, encode_image


# Create your models here.


class Replacer:
    def __init__(self, first_operand, result):
        self.first_operand = first_operand
        self.result = result
        self.operation = 'replace'


class ImageFromPillow:
    def __init__(self, image_base64, encoding):
        self.image_base64 = base64
        self.encoding = encoding
