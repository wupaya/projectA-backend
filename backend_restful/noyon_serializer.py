from rest_framework import serializers
class NoyonSerializer(serializers.Serializer):
    message = serializers.charField()