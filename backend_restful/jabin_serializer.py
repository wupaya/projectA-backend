from rest_framework import serializers 
class JabinSerializer(serializers.Serializer):
  greetings = serializers.CharField()