from backend_restful.db import users
import pymongo
from bson.objectid import ObjectId
from pprint import pprint

mongodb_url = "mongodb+srv://anamika:1234@cluster0-t3qae.mongodb.net/test?retryWrites=true"

class join_institute:
    response = {}
    def __init__(self, data={}):
        #query database for dashboard info
        #str(users.find_one({"$and":[{"email": "mhsn06@gmail.com"},{"password": "1234"}]}))
        client = pymongo.MongoClient(mongodb_url)
        db = client.test
        education = db.education
        user_id = data.get("user_info")
        #pprint(user_id)


        #this is to avoid ObjectId not serializer error
        #query_result["_id"] = user_id
        query_result = { 
            "_id":ObjectId(user_id),
            "associated": [
            {"_id": ObjectId(), "short_name":"BRUR", "long_name":"Begum Rokeya University, Rangpur", "designations":[
                {"_id": ObjectId(), "title":"Parent", "tags":[
                    {"_id":ObjectId(), "title":"", "tasks":[
                        {"_id":ObjectId(), "title":""},
                        {"_id":ObjectId(), "title":""},
                        {"_id":ObjectId(), "title":""},
                    ]},
                    {"_id":ObjectId(), "title":"", "tasks":[
                        {"_id":ObjectId(), "title":""},
                        {"_id":ObjectId(), "title":""},
                        {"_id":ObjectId(), "title":""},
                    ]},
                ]},
                {"_id": ObjectId(), "title":"Teacher", "tags":[
                    {"_id":ObjectId(), "title":"", "tasks":[
                        {"_id":ObjectId(), "title":""},
                        {"_id":ObjectId(), "title":""},
                        {"_id":ObjectId(), "title":""},
                    ]},
                    {"_id":ObjectId(), "title":"", "tasks":[
                        {"_id":ObjectId(), "title":""},
                        {"_id":ObjectId(), "title":""},
                        {"_id":ObjectId(), "title":""},
                    ]},
                ]}
            ]}
            ]
        }
        #pprint("user id "+ user_id)
        res = education.update_one({"_id":ObjectId(user_id)}, {"$set": {"associated":query_result.get("associated", [])}}, upsert=True)

        #pprint(res)

        if res.matched_count>0:
            self.response={"s":"success"}
        

        self.response={"s":"fail"}