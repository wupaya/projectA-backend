from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .noyon import Noyon
from .noyon import Noyon2
from .noyon import Noyon3
from .noyon import Noyon4
from .noyon import Noyon5
from .noyon_serializer import NoyonSerializer
from .noyon_serializer import Noyon2Serializer
from .noyon_serializer import Noyon3Serializer
from .noyon_serializer import Noyon4Serializer
from .noyon_serializer import Noyon5Serializer

class NoyonView(APIView):
    '''
    **Name**
    ----
      _Hey, I am Mahfujar Rahman Noyon._
 
    **Education**
    ----
    * **University/College: **
      _Rangpur Engineering College._

    * **Department**
      _Computer Science of Engineering_

    * **Batch**
      _1st Batch_
    
    * **Session**
      _2016-17_

    '''
    def get(self,request):
        serializer = NoyonSerializer(Noyon())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = NoyonSerializer(Noyon())
        return Response (serializer.data, status.HTTP_200_OK)
        
class Noyon2View(APIView):
    def get(self,request):
        serializer = Noyon2Serializer(Noyon2())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Noyon2Serializer(Noyon2())
        return Response (serializer.data, status.HTTP_200_OK)
        
class Noyon3View(APIView):
    def get(self,request):
        serializer = Noyon3Serializer(Noyon3())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Noyon3Serializer(Noyon3())
        return Response (serializer.data, status.HTTP_200_OK)

class Noyon4View(APIView):
    def get(self,request):
        serializer = Noyon4Serializer(Noyon4())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Noyon4Serializer(Noyon4())
        return Response (serializer.data, status.HTTP_200_OK)
        
class Noyon5View(APIView):
    def get(self,request):
        serializer = Noyon5Serializer(Noyon5())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Noyon5Serializer(Noyon5())
        return Response (serializer.data, status.HTTP_200_OK)
