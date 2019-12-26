from backend_restful.db import users
from backend_restful.DBHandler import DBHandler
from bson.objectid import objectId
from pprint import pprint
from rest_framework import serializers
import json


class list_recieved_invitations:
    response = {}
    def __init__(self, data={}):

        client = DBHandler.get_database_client()
        db = client.test
        education = db.education
        user_id = data.get("user_info")

        query_result = education.find_one(
            {
                "id" : objectId(user_id)
            },
            {
                "invitations" : 1
            }
            )
             self.response=json.loads(json.dumps(query_result, default=str))
             