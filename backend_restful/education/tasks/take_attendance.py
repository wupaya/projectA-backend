from backend_restful.DBHandler import DBHandler
from bson.objectid import ObjectId
from pprint import pprint
from rest_framework import serializers

'''
user requirment: User take attendance
system requirement:
    1. user list student task to get a list of students
    2. perform taking attendance
    3. store in attendance collection
'''

class take_attendance:
    response = None
    def __init__(self, data={}):
        client = DBHandler.get_database_client()
        db = client.test

        attendance_history_object = {
            "association_id":"",
            "year":[
                {
                    "month":[
                        {
                            "days": [
                                {
                                    "association_id": "",
                                    "statues": "present"                                    
                                }
                            ]
                        }
                    ]
                }
            ],
            "":"",
            "":"",
            "":""
        }

        self.response = {"res": db.attendance.insert_one({"test":"working!"}).inserted_id}
        #serialize data
        #perform mass store query in student_attendance_history and attendance_statistics collection
        #return store status




class AttendanceSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    status = serializers.CharField() # instititue id
class TakeAttendanceSerializer(serializers.Serializer):
    attendances = serializers.ListField(child=AttendanceSerializer())
