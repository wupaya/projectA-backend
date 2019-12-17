from backend_restful.DBHandler import DBHandler
from bson.objectid import ObjectId
from pprint import pprint
from rest_framework import serializers


'''
user requirement: user can invite people to join institute
system requirement:
    1. user enter contact info phone no, name, and prefered designation
    2. system send short message with instruction to register and join
    3. Invited user enter necessary info to the system 
    4. System generate an invitation verification code who sent invitation
    5. Invited user collect verification code over phone/visit to office/email or by any means
    6. Invited user enter the code to the system and verified

this task use system requirement 1,2
'''

class add_people:
    response = {}

    def __init__(self, data={}):

        serializer = AddPeopleSerializer(data=data["data"])

        if serializer.is_valid():
            #debug
            #self.response = serializer.validated_data
            #return
            
            '''
            1. query user by phone no
            2. if not found create an user in user collection
            3. create a document in education collection with user id
                attributes:
                
            4. Enque to sms/email send system
            '''
            client = DBHandler.get_database_client()

            user_collection = client.user
            user_query_result = user_collection.find_one()
            if user_query_result is None:
                #insert user in user collection and get the id
                invited_user_id = user_collection.insert_one()
            else:
                invited_user_id = user_query_result.user_id

            #inserting into education collection

            ppageid = client.public_pages.find_one({"_id": ObjectId(serializer.validated_data.get("institute_id"))})
            if(ppageid is None):
                self.response={"status_code":"page_not_found", "default_description":"no such thing exits in the system"}
                return
            
            stored_designations = ppageid.get("designation") 
            incoming_designations = serializer.validated_data.get("designations")
            matched_designations = []

            for designations in incoming_designations:
                for designation in stored_designations:
                    #pprint(designation)
                    if(designations==designation["title"]):
                        matched_designations.append(designation)

            

            associate_institute_document_object = {
                "_id": ObjectId(),
                "long_name": ppageid.get("page_title"),
                "description": ppageid.get("description"),
                "designations": matched_designations,
                "invitor" : "TODO"
            }

            education_collection = client.education

            #pprint("user id "+ user_id)
            res = education_collection.update_one({
                "_id":ObjectId(invited_user_id)
                }, {
                    "$push": {
                        "associated":associate_institute_document_object
                    }
                }, upsert=True)

            #pprint(res)
            if res.matched_count>0:
                #add to send message database
                education_doc_id = ""
                invitation_message_object = {
                    "invitation_id": education_doc_id,
                    "status" : "pending"
                }
                invitation_id = client.invitation_queue.insert_one(invitation_message_object)
                if invitation_id is None:
                    self.response={"error":"something went wrong"}
                else:
                    self.response={"status":"success"}
            else:
                self.response={"s":"fail"}
        else:
            self.response = {"error": serializer.errors}

class AddPeopleSerializer(serializers.Serializer):
    phone_no = serializers.CharField()
    name = serializers.CharField()
    institute_id = serializers.CharField()
    designations = serializers.ListField(child=serializers.CharField())