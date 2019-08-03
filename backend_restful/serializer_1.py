from rest_framework import serializers 
class JabinSerializer(serializers.Serializer):
  greetings = serializers.CharField()
class JabinSerializer2(serializers.Serializer):
  greetings = serializers.CharField()
class JabinSerializer3(serializers.Serializer):
  greetings = serializers.CharField()
class JabinSerializer4(serializers.Serializer):
  greetings = serializers.CharField()
  
class JabinParameterInput(serializers.Serializer):
    num1 = serializers.IntegerField()
    num2 = serializers.IntegerField()
 
 
class jabinParameterOutput(serializers.Serializer):
    sum = serializers.IntegerField()

    
class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    username = serializers.CharField()
    name = serializers.CharField()
    phone_no = serializers.CharField()