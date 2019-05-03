from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .jabin import Jabin,Jabin2,Jabin3,Jabin3
from .jabin_serializer import JabinSerializer,JabinSerializer2,JabinSerializer3,JabinSerializer3

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
class JabinView3(APIView):
    def get(self,request):
        serializer = JabinSerializer3(Jabin3())
        return Response (serializer.data,status.HTTP_200_OK)
    def post(self,request):
        serializer = JabinSerializer3(Jabin3())
        return Response (serializer.data,status.HTTP_200_OK)
class JabinView3(APIView):
    def get(self,request):
        serializer = JabinSerializer3(Jabin3())
        return Response (serializer.data,status.HTTP_200_OK)
    def post(self,request):
        serializer = JabinSerializer3(Jabin3())
        return Response (serializer.data,status.HTTP_200_OK)