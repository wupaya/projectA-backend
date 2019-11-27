from backend_restful.db import users
import pymongo
from bson.objectid import ObjectId
from pprint import pprint
from rest_framework import serializers
import json

mongodb_url = "mongodb+srv://anamika:1234@cluster0-t3qae.mongodb.net/test?retryWrites=true"

class tags:
    response = {}
    def __init__(self, data={}):
        data["associated"] = "5ddd62ffd8639286d599dcd6"
        data["designations"] = "5ddd62ffd8639286d599dcd7"
        #query database for dashboard info
        client = pymongo.MongoClient(mongodb_url)
        db = client.test
        education = db.education
        user_id = data.get("user_info")
        #pprint(user_id)
        query_result = education.find_one(
              {"_id" : ObjectId(user_id),
              "associated._id": ObjectId(data.get("associated")),
              "associated.designations._id": ObjectId(data.get("designations"))
              },
              {"associated.designations.tags":1,
               "associated.designations.tags.title":1,
               "associated.designations.tags._id":1,
               }
        )
        #this is to avoid ObjectId not serializer error
        #query_result["_id"] = user_id
        print("showing results")
        pprint(query_result)
        # query_result = { 
        #     "_id":ObjectId(user_id),
        #     "associated": [
        #     {"id": 1, "short_name":"BRUR", "long_name":"Begum Rokeya University, Rangpur", "designation":"Parent",
        #     "status": "joined",
        #     "join_date": "July 1st 2019",
        #     "allowed_services": [
        #     { "id": 1, "designation": "Parent" },
        #     { "id": 2, "designation": "Teacher" } ]},
        #     {"id": 2, "short_name":"RGC", "long_name":"Rangpur Government College, Rangpur", "designation":"Parent",
        #     "status": "joined",
        #     "join_date": "July 1st 2019",
        #     "allowed_services": [
        #     { "id": 1, "designation": "Parent" },
        #     { "id": 2, "designation": "Teacher" } ]},
        #     ]
        # }

        #query database for associates
        #{"_id":ObjectId(user_id)}
        #post_id = education.insert_one(query_result).inserted_id
        
        #print(json.dumps(query_result, cls=JSONEncoder))
        self.response=json.loads(json.dumps(query_result, default=str))