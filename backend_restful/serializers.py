from rest_framework import serializers
from .my_app import Hello, HelloParam

class HelloSerializer(serializers.Serializer):
    greetings = serializers.CharField(required=False, max_length=200)
class HelloParamSerializer(serializers.Serializer):
    param1 = serializers.CharField(required=True, max_length=200)
    param2 = serializers.CharField(required=True, max_length=200)
class HelloMessageSerializer(serializers.Serializer):
    message = serializers.CharField(required=True, max_length=200)
	# def create(self, validated_data):
		# return HelloParam.objects.create(**validated_data)
		
class SignUpInputDataSerializer(serializers.Serializer):
	email = serializers.CharField(required=True)
	password = serializers.CharField(required=True)
	phone_no = serializers.CharField(required=True)
	address = serializers.CharField(required=True)
	sex = serializers.CharField(required=True)
	profession = serializers.CharField(required=True)
	date_of_birth = serializers.CharField(required=True)