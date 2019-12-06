from backend_restful.db import users
import pymongo
from bson.objectid import ObjectId
from pprint import pprint
from .task_serializer import JoinInstituteSerializer

mongodb_url = "mongodb+srv://anamika:1234@cluster0-t3qae.mongodb.net/test?retryWrites=true"

class join_institute:
    response = {}
    def __init__(self, data={}):

        serializer = JoinInstituteSerializer(data=data)

        if serializer.is_valid():
            public_page_id = serializer.validated_data.get("institute_id")
            designations = serializer.validated_data.get("designations")

            #query database for dashboard info
            #str(users.find_one({"$and":[{"email": "mhsn06@gmail.com"},{"password": "1234"}]}))
            client = pymongo.MongoClient(mongodb_url)
            db = client.test
            education = db.education
            user_id = data.get("user_info")
            public_pages = db.public_pages
            #query if already exist
            ppageid = public_pages.find_one({"_id": ObjectId(public_page_id)})

            if(ppageid is None):
            #return not found error
            return Response({"status_code":"page_not_found", "default_description":"no such thing exits in the system"}, status=status.HTTP_200_OK)

            #this is to avoid ObjectId not serializer error
            #query_result["_id"] = user_id
            query_result = { 
                "_id":ObjectId(user_id),
                "associated": [
                {"_id": ObjectId(), "long_name": ppageid.get("page_title"), "page_type": ppageid.get("type_of_institute"), "description": ppageid.get("description"), "designations":[
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