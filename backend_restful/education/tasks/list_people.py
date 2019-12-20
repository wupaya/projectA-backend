from backend_restful.DBHandler import DBHandler
from bson.objectid import ObjectId
from pprint import pprint
from rest_framework import serializers

'''
user requirment: Description return a list of people based on filters
system requirement:
    1. 
'''

class list_people:
    response = None
    def __init__(self, data={}):
        #serialize data
        #perform aggregate query based on filters
        #return result
        pass




class listPeopleSerializer(serializers.Serializer):
    people_type = serializers.CharField() # student/teacher/commetee member/guardian/alumni
    institute_id = serializers.CharField() # instititue id