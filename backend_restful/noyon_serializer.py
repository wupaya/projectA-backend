from rest_framework import serializers
class NoyonSerializer(serializers.Serializer):
    greetings = serializers.CharField()

class Noyon2Serializer(serializers.Serializer):
    greetings = serializers.CharField()

class Noyon3Serializer(serializers.Serializer):
    greetings = serializers.CharField()

class Noyon4Serializer(serializers.Serializer):
    greetings = serializers.CharField()

class Noyon5Serializer(serializers.Serializer):
    greetings = serializers.CharField()
    
    
class NoyonParameterInput(serializers.Serializer):
    num1 = serializers.IntegerField()
    num2 = serializers.IntegerField()
    
class NoyonParameterOutput(serializers.Serializer):
    sum = serializers.IntegerField()