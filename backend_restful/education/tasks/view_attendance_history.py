from backend_restful.DBHandler import DBHandler
from bson.objectid import ObjectId
from pprint import pprint
from rest_framework import serializers

'''
user requirment: View attendance history
'''

class view_attendance_history:
    response = None
    def __init__(self, data={}):
        #serialize data
        #perform query in student_attendance_history
        #return result
        pass




class listPeopleSerializer(serializers.Serializer):
    student_id = serializers.CharField() #