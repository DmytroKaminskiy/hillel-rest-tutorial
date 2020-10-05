from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorldView(APIView):
    def get(self, request, format=None):  # noqa
        """
        Возвращает базовый ответ в виде {"data": "Hello, world!"}
        """
        return Response({"data": "Hello, world!"})
