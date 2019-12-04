from rest_framework import serializers

class JoinInstituteSerializer(serializers.ListField):
    institute_id = serializers.CharField()
    designations = serializers.ListField()
