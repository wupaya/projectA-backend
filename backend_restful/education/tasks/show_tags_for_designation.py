from backend_restful.db import users
import pymongo
from bson.objectid import ObjectId
from pprint import pprint

mongodb_url = "mongodb+srv://anamika:1234@cluster0-t3qae.mongodb.net/test?retryWrites=true"

class dashboard:
    response = {}
    def __init__(self, data={}):
        #query database for dashboard info
        #str(users.find_one({"$and":[{"email": "mhsn06@gmail.com"},{"password": "1234"}]}))
        client = pymongo.MongoClient(mongodb_url)
        db = client.test
        education = db.education
        user_id = data.get("user_info")
        pprint(user_id)
        query_result = education.find_one(
              {"_id" : ObjectId(user_id), "associated": {"$elemMatch":{"_id": data.get(associated),"$elemMatch":{"designation":"parent"}},""},
              {"_id":1,
              "tags":1}
        )

        #this is to avoid ObjectId not serializer error
        query_result["_id"] = user_id
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
        



        self.response=query_result