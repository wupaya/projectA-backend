from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .proton import Proton
from .proton import proton2
from .proton import Proton3
from .proton import Proton4
from .proton import Proton5
from .proton_serializer import ProtonSerializer
from .proton_serializer import Proton2Serializer
from .proton_serializer import Proton3Serializer
from .proton_serializer import Proton4Serializer
from .proton_serializer import Proton5Serializer

class ProtonView(APIView):
    def get(self,request):
        serializer = ProtonSerializer(Proton())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = ProtonSerializer(Proton())
        return Response (serializer.data, status.HTTP_200_OK)
        
class Proton2View(APIView):
    def get(self,request):
        serializer = Proton2Serializer(Proton2())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Proton2Serializer(Proton2())
        return Response (serializer.data, status.HTTP_200_OK)
        
class Proton3View(APIView):
    def get(self,request):
        serializer = Proton3Serializer(Proton3())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Proton3Serializer(Proton3())
        return Response (serializer.data, status.HTTP_200_OK)

class Proton4View(APIView):
    def get(self,request):
        serializer = proton4Serializer(Proton4())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Proton4Serializer(Proton4())
        return Response (serializer.data, status.HTTP_200_OK)
        
class Proton5View(APIView):
    def get(self,request):
        serializer = Proton5Serializer(Proton5())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Proton5Serializer(Proton5())
        return Response (serializer.data, status.HTTP_200_OK)
