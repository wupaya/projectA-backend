from backend_restful.db import users
from backend_restful.DBHandler import DBHandler
from bson.objectid import ObjectId
from pprint import pprint
from rest_framework import serializers

class create_public_page:
    response = {}
    def __init__(self, data={}):

        serializer = PublicPageSerializer(data=data["data"])

        if serializer.is_valid():
            #query database 
            client = DBHandler.get_database_client()
            db = client.test
            public_pages = db.public_pages
            #user_id = data.get("user_info")
            found_page = public_pages.find_one({"page_title": serializer.validated_data.get("page_title")})
            if(found_page is None):
                #serializer.validated_data["_id"] = "brur"
                post_id = public_pages.insert_one(serializer.validated_data).inserted_id
                self.response = {"status_code":"page_creation_successfull", "default_description":"successfully created page", "id": str(post_id)}
            else:
                self.response = {"status_code":"registration_failed", "default_description":"already exist", "id": str(found_page["_id"])}
        else:
            self.response ={"error": serializer.errors}

class PublicPageSerializer(serializers.Serializer):
    page_title = serializers.CharField()
    type_of_institute = serializers.CharField()
    founding_date = serializers.CharField()
    address_district = serializers.CharField()
    address_upozila = serializers.CharField()
    no_of_stakeholder = serializers.CharField()
    description = serializers.CharField()