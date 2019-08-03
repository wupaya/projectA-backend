from rest_farmework import serializers
class login_input(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.PasswordField()
    
class login_output(serializers.Serializer):
    token = serializers.