from backend_restful.DBHandler import DBHandler
from rest_framework import serializers
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from random import randint


class InvitePeopleSerializer(serializers.Serializer):
    phone_no = serializers.IntgerField()
    institute_id = serializers.CharField()
    designation = serializers.ListField()


class invite_people:
    response = {}

    def __init__(self, data={}):
        serializer = InvitePeopleSerializer(data=data):
        if serializer.is_valid():
            users_incoming_phone_no = serializer.validated_data.get("phone_no")

            # query database for dashboard info
            #str(users.find_one({"$and":[{"email": "mhsn06@gmail.com"},{"password": "1234"}]}))
            client = DBHandler.get_database_client()
            db = client.test
            education = db.education
            user_id = data.get("user_info")
            users = db.users

            serched_phone_number = user_id.find_one(
                {"_id": ObjectId(users_incoming_phone_no)})

            if(serched_phone_number is None):
                # todo store user phon
                new_user_id = users.insert_one(
                    {"phone_no": users_incoming_phone_no}).inserted_id

                invitation_document_object = {
                    "_id": ObjectId(),
                    "phone_no": serializer.validated_data.get("phone_no"),
                    "expired_date": datetime.now()+timedelta(hours=48),
                    "invitation_from": user_id,
                    "institute_id": serializer.validated_data.get("institute_id"),
                    "designations": serializer.validated_data.get("designation"),
                    "verification_code": randint(1000, 9999)  
                }
                res = education.update_one({"_id": ObjectId(user_id)}, {"$push":
                {"invitation":invitation_document_object}}, upsert=True)

                invitation_id = education.find_one({"_id": ObjectId(invitation_document_object)

                #sms queue collection
                sms_queue = db.sms_queue
                sms_queue.insert_one({"_id":ObjectId(), "invitation_id": invitation_id, "send_status": "pending"})

                self.response = {"success"}
        else:
            self.response = serializer.errors

