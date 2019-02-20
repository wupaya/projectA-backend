from rest_framework import serializers
class NoyonSerializer(serializers.Serializer):
    greetings = serializers.CharField()