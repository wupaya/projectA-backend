from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class NoyonView(APIView):
    def get(self,request):
        serializer = NoyonSerializer(Noyon())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = NoyonSerializer(Noyon())
        return Response (serializer.data, status.HTTP_200_OK)