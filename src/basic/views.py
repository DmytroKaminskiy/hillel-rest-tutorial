from basic import status_codes
from basic.utils import get_client_ip

from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorldView(APIView):
    def get(self, request, format=None):  # noqa
        """
        Возвращает базовый ответ в виде {"data": "Hello, world!"}
        """
        return Response({"data": "Hello, world!"})


class StatusCodesView(APIView):
    def get(self, request, format=None):  # noqa
        """
        Возвращает список возможных статус ответов сервера с группировкой по классам
        """
        return Response({'data': status_codes.CODES})


class StatusCodeInfoView(APIView):
    def get(self, request, status_code, format=None):  # noqa
        """
        Возвращает детальную информацию о статусе ответа
        """
        status_info = status_codes.STATUSES.get(status_code)
        if status_info:
            return Response({'data': status_info})
        return Response({'detail': f'Status Code "{status_code}" not found.'}, status=404)


class GetMyIpView(APIView):
    def get(self, request, format=None):  # noqa
        """
        Возвращает IP адресс клиента
        """
        ip = get_client_ip(request)

        if ip:
            return Response({'data': ip})

        return Response({'detail': 'Ip is not detected!'}, status=404)
