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
            incoming_designations = serializer.validated_data.get("designations")

            #query database for dashboard info
            #str(users.find_one({"$and":[{"email": "mhsn06@gmail.com"},{"password": "1234"}]}))
            client = pymongo.MongoClient(mongodb_url)
            db = client.test
            education = db.education
            user_id = data.get("user_info")
            public_pages = db.public_pages

            # Inserting a dummy public_page object for testing
            if(1):
                data = {"_id": ObjectId(), "page_title":"Begum Rokeya university", "description": "BRUR Description", "designation":{
                    {"_id": ObjectId(), "title":"parents", "tasks":
                    {{
                        {"_id": ObjectId()}
                        {"title":"task11_name"}
                    }
                    {
                        {"_id": ObjectId()}
                        {"title":"task12_name"}
                    }}}
                    {"_id":ObjectId(), "title":"teacher","tasks":
                    {{
                        {"_id": ObjectId()}
                        {"title":"task21_name"}
                    }
                    {
                        {"_id": ObjectId()}
                        {"title":"task22_name"}
                    }}}}
                

            #query if already exist
            ppageid = public_pages.find_one({"_id": ObjectId(id)})
            if(ppageid is None):
                #return not found error and store ppageid
                ppageid = public_pages.insert_one
                return Response({"status_code":"page_not_found", "default_description":"no such thing exits in the system"}, status=status.HTTP_200_OK)

            stored_designations = ppageid.get("designation") 
            matched_designations = []
            for designations in incoming_designations:
                for designation in stored_designations:
                    if(designations==designation):
                        matched_designations.append(designation)
            #this is to avoid ObjectId not serializer error
            #query_result["_id"] = user_id
            associate_institute_document_object = { 
                "_id":ObjectId(user_id),
                "associated": [
                {"_id": ObjectId(), "long_name": ppageid.get("page_title"), "description": ppageid.get("description"), "designations": matched_designations
            }
            #pprint("user id "+ user_id)
            res = education.update_one({"_id":ObjectId(user_id)}, {"$push": {"associated":associate_institute_document_object}}, upsert=True)

            #pprint(res)

            if res.matched_count>0:
                self.response={"s":"success"}
            

            self.response={"s":"fail"}