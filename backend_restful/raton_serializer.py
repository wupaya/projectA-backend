from rest_framework import serializers 
class RatonSerializer(serializers.Serializer):
  greetings = serializers.CharField()