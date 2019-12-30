from rest_framework import serializers
from backend_restful.DBHandler import DBHandler
from bson.objectid import ObjectId
import json
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
                #print(str(stored_invitation["_id"]))
                #print(stored_invitation["_id"])
                if(str(stored_invitation["_id"]) == serializer.validated_data.get("invitation_id")):
                    self.response = json.loads(json.dumps(stored_invitation, default=str))
                    return
                else:
                    self.response = json.loads(json.dumps({"message": "something went wrong."}, default=str))
        else:
            self.response = serializer.errors