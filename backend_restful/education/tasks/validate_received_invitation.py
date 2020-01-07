from rest_framework import serializers
from bson.objectid import ObjectId
from backend_restful.DBHandler import DBHandler
import json
class IncomiingDataSerializer(serializers.Serializer):
    verification_code = serializers.IntegerField()
    invitation_id = serializers.CharField()
class validate_received_invitation:
    response = {}
    def __init__(self, data={}):
        serializer = IncomiingDataSerializer(data = data)
        if serializer.is_valid():
            client = DBHandler.get_database_client()
            db = client.test
            education = db.education
            user_id = data.get("user_info")
            public_pages = db.public_pages
            #searched_invitation = education.find_one({"_id":ObjectId(serializer.validated_data.get("invitation_id"))})
            #searched_user_id = education.find_one({"_id":ObjectId(user_id)})
            searched_user_id = education.find_one({"_id":ObjectId("5e08ce2ffebc801b83cd2579")})
            #print(searched_user_id)
            invitation_list = searched_user_id.get("invitations")
            incoming_invitation_id = serializer.validated_data.get("invitation_id")

            for stored_invitation in invitation_list:
                #print(stored_invitation)
                #print(incoming_invitation_id)
                #print(str(stored_invitation["_id"]))
                if(str(stored_invitation["_id"]) == incoming_invitation_id):
                    if(serializer.validated_data.get("verification_code") == stored_invitation.get("verification_code")):
                        #print(stored_invitation)
                        institute_id = stored_invitation.get("institute_id")
                        #institute_id = "5df85e5f8b98b8fc21f45162"
                        searched_institute_id = public_pages.find_one({"_id":ObjectId(institute_id)})
                        #print(searched_institute_id)
                        invited_designation = stored_invitation.get("designations")
                        ppage_designation = searched_institute_id.get("designation")
                        #print(ppage_designation)
                        matched_designations = []

                        for p_designation in ppage_designation:
                            #print(p_designation)
                            for i_designation in invited_designation:
                                #print(i_designation)
                                if (i_designation == p_designation.get("title")):
                                    matched_designations.append(p_designation)

                        associate_institute_document_object = {
                            "institute_id": searched_institute_id,
                            "long_name": searched_institute_id.get("page_title"),
                            "description": searched_institute_id.get("description"),
                            "designations":matched_designations
                        }

                        res = education.update_one({"_id":ObjectId(user_id)}, {"$push": {"associated":associate_institute_document_object}}, upsert=True)
                        
                        #print(matched_designations)
                        tags = []
                        for designation in  matched_designations:
                            tags.append(designation.get("tags"))
                            
                        if res.matched_count>0:
                            self.response= json.loads(json.dumps(tags,default=str))
                            return
                        else:
                            self.response={"message":"something went wrong"}
                    else:
                        self.response={"message":"verification code error"}
                else:
                    self.response={"message":"invitation not found"}
        else:
            self.response = serializer.errors