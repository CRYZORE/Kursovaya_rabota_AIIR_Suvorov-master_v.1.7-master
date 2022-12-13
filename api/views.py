import time

from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView

import ReplaceTextApp
from ReplaceTextApp.ReplaceTextFunc.func import replacing
from .models import Replacer, ImageFromPillow
from .serializers import ReplacerSerializer, ImageFromPillowSerializer


class ReplacerView(APIView):
    @extend_schema(request=ReplacerSerializer, responses=ReplacerSerializer)
    def get(self, request, s):
        replacer = Replacer(s, ReplaceTextApp.ReplaceTextFunc.replacing(s))

        serializer_for_request = ReplacerSerializer(instance=replacer)

        return Response(serializer_for_request.data)


class ImageFromPillowView(APIView):

    def get(self, request):
        ts = str(time.time()).replace('.', '_')
        image_path = f"./{ts}.jpg"
        ReplaceTextApp.generate_img(image_path)
        image_string = ReplaceTextApp.encode_image(image_path)

        image_result = ImageFromPillow(image_string, 'unicode_escape')
        serializer_for_request = ImageFromPillowSerializer(instance=image_result)

        return Response(serializer_for_request.data)
