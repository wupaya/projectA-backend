from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .raton import Raton
from .raton_serializer import RatonSerializer

class RatonView(APIView):
    def get(self,request):
        serializer = RatonSerializer(Raton())
        return Response (serializer.data,status.HTTP_200_OK)
    def post(self,request):
        serializer = RatonSerializer(Raton())
        return Response (serializer.data,status.HTTP_200_OK)