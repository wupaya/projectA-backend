from rest_framework import serializers
class SubSerializer(serializers.serializer):
    message = serializers.charField()