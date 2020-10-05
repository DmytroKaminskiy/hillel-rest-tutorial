from basic import status_codes

from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorldView(APIView):
    def get(self, request, format=None):  # noqa
        """
        Возвращает базовый ответ в виде {"data": "Hello, world!"}
        """
        return Response({"data": "Hello, world!"})


class StatusCodeView(APIView):
    def get(self, request, format=None):  # noqa
        """
        Возвращает список возможных статус ответов сервера с группировкой по классам
        """
        return Response({'data': status_codes.CODES})
