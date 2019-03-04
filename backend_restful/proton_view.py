from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .proton import Proton
from .proton_serializer import ProtonSerializer

class ProtonView(APIView):
    def get(self,request):
        serializer = ProtonSerializer(Proton())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = ProtonSerializer(Proton())
        return Response (serializer.data, status.HTTP_200_OK)