from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .jabin import Jabin,Jabin2
from .jabin_serializer import JabinSerializer,JabinSerializer2

class JabinView(APIView):
    def get(self,request):
        serializer = JabinSerializer(Jabin())
        return Response (serializer.data,status.HTTP_200_OK)
    def post(self,request):
        serializer = JabinSerializer(Jabin())
        return Response (serializer.data,status.HTTP_200_OK)
class JabinView2(APIView):
    def get(self,request):
        serializer = JabinSerializer2(Jabin2())
        return Response (serializer.data,status.HTTP_200_OK)
    def post(self,request):
        serializer = JabinSerializer2(Jabin2())
        return Response (serializer.data,status.HTTP_200_OK)