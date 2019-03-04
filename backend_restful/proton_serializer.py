from rest_framework import serializers
class ProtonSerializer(serializers.Serializer):
    greetings = serializers.CharField()