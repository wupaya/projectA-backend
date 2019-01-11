from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer, HelloParamSerializer, HelloMessageSerializer
from .my_app import Hello, HelloParam
	
	
class Hello2View(APIView):
     '''
	 simple use of response no serialization
	 '''
     def get(self, request):
        return Response({"hello":"world"})
		
class HelloView(APIView):
    '''
	simple use of serialization
	'''
    def get(self, request, pk=None):
        hello = Hello(name=request.query_params.get('name'))
        serializer = HelloSerializer(hello)
        return Response(serializer.data)
		
class NiceUrlParamView(APIView):
     '''
	 simple use of nice url parameters
	 '''
     def get(self, request, pk=None):
        return Response({"pk":pk})		
		
class ValidateParamView(APIView):
    '''
	simple use of deserializers, validation and serialization
	'''
    def post(self, request, pk=None):
        serializer = HelloParamSerializer(data=request.data)
        if serializer.is_valid():
          helloparamobject = HelloParam(serializer.validated_data.get('param1'),serializer.validated_data.get('param2'))
          return Response(HelloMessageSerializer(helloparamobject).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)