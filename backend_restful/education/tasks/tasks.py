from backend_restful.db import users
from backend_restful.DBHandler import DBHandler
import pymongo
from bson.objectid import ObjectId
from pprint import pprint
from rest_framework import serializers
import json

class TasksSerializer(serializers.Serializer):
    associated = serializers.CharField()
    designation = serializers.CharField()
    tag = serializers.CharField()

class tasks:
    response = {}
    def __init__(self, data={}):
        #data["associated"] = "5ddd62ffd8639286d599dcd6"
        #data["designation"] = "5ddd62ffd8639286d599dcd7"
        #data["tag"] = "5ddd62ffd8639286d599dcd8"
        serializer = TasksSerializer(data=data)
        if serializer.is_valid():
            #query database for dashboard info
            client = DBHandler.get_database_client()
            db = client.test
            education = db.education
            user_id = data.get("user_info")
            
            query_result = education.find_one(
                {
                "_id" : ObjectId(user_id)
                }
                )

            print("showing results")
            pprint(query_result)

            for associate in query_result["associated"]:
                if serializer.validated_data.get("associated") == str(associate.get("_id")):
                    for designation in associate["designations"]:
                        if serializer.validated_data.get("designation") == str(designation.get("_id")):
                            for tag in designation["tags"]:
                                if serializer.validated_data.get("tag") == str(tag.get("_id")):
                                    self.response=json.loads(json.dumps(tag, default=str))
                                    return

            self.response=json.loads(json.dumps({"error": "retriving_tast_list"}, default=str))
        else:
            self.response = serializer.errors