from backend_restful.DBHandler import DBHandler
from bson.objectid import ObjectId
from pprint import pprint
from rest_framework import serializers
import json

class get_associated_institues:
    response = {}
    def __init__(self, data={}):
        #query database for dashboard info
        client = DBHandler.get_database_client()
        db = client.test
        education = db.education
        user_id = data.get("user_info")
        #pprint(user_id)
        query_result = education.find_one(
              {"_id" : ObjectId(user_id)},
              {"_id":0, "associated.designations.tags":0 }
        )
        #print(json.dumps(query_result, cls=JSONEncoder))
        self.response=json.loads(json.dumps(query_result, default=str))