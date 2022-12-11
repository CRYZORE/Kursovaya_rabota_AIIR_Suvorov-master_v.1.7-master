import time

from django.shortcuts import render
from rest_framework.response import Response
from summary.sum.func import generate_img, encode_image
from rest_framework.views import APIView
from .models import Replacer, ImageFromPillow
from .serializers import ReplacerSerializer, ImageFromPillowSerializer
from drf_spectacular.utils import extend_schema
from summary import sum
import summary


class ReplacerView(APIView):
    @extend_schema(request=ReplacerSerializer, responses=ReplacerSerializer)
    def get(self, request, s):
        replacer = Replacer(s, summary.summary(s))

        serializer_for_request = ReplacerSerializer(instance=replacer)

        return Response(serializer_for_request.data)


class ImageFromPillowView(APIView):

    def get(self, request):
        ts = str(time.time()).replace('.', '_')
        image_path = f"./{ts}.jpg"
        summary.generate_img(image_path)
        image_string = summary.encode_image(image_path)

        image_result = ImageFromPillow(image_string, 'unicode_escape')
        serializer_for_request = ImageFromPillowSerializer(instance=image_result)

        return Response(serializer_for_request.data)
