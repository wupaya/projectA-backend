from backend_restful.db import users
import pymongo
from bson.objectid import ObjectId
from pprint import pprint
from rest_framework import serializers
import json

mongodb_url = "mongodb+srv://anamika:1234@cluster0-t3qae.mongodb.net/test?retryWrites=true"

class dashboard:
    response = {}
    def __init__(self, data={}):
        #query database for dashboard info
        client = pymongo.MongoClient(mongodb_url)
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