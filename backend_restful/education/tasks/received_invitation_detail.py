from rest_framework import serializers
from backend_restful.DBHandler import DBHandler
from bson.objectid import ObjectId
from pprint import pprint
class IncomingDataSerializer(serializers.Serializer):
    invitation_id = serializers.CharField()

class received_invitation_detail:
    response = {}
    def __init__(self, data={}):
        serializer = IncomingDataSerializer(data = data)

        if serializer.is_valid():
            client = DBHandler.get_database_client()
            db = client.test
            education = db.education
            user_id = data.get("user_info")

            #searched_user_id = education.find_one({"_id":ObjectId(user_id)})
            searched_user_id = education.find_one({"_id":ObjectId("5e08ce2ffebc801b83cd2579")})

            invitation_list = searched_user_id.get("invitations")

            for stored_invitation in invitation_list:
                if(stored_invitation["_id"] == serializer.validated_data.get("invitation_id")):
                    self.response = stored_invitation
                else:
                    self.response = {"message": "something went wrong."}
        else:
            self.response = serializer.errors