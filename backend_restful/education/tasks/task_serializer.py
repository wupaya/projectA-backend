from rest_framework import serializers

class JoinInstituteSerializer(serializers.Serializer):
    institute_id = serializers.CharField()
    designations = serializers.ListField()
