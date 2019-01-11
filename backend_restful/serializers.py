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