from rest_framework import serializers
from .my_app import SignupRequest
        
class SignUpInputDataSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    phone_no = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    sex = serializers.CharField(required=True)
    profession = serializers.CharField(required=True)
    date_of_birth = serializers.CharField(required=True)

    def create(self, validated_data):
        #or query from database
        return SignupRequest(**validated_data)
        
    def update(self, instance, validated_data):
        #update current instance
        return instance
        
    def save(self):
        #save to database
        pass
class SubSerializer(serializers.Serializer):
    message = serializers.CharField()