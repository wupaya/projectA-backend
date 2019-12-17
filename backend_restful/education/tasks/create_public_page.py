from backend_restful.DBHandler import DBHandler
from bson.objectid import ObjectId
from pprint import pprint
from rest_framework import serializers


class create_public_page:
    response = {}

    def __init__(self, data={}):

        serializer = PublicPageSerializer(data=data["data"])

        if serializer.is_valid():
            # query database
            client = DBHandler.get_database_client()
            db = client.test
            public_pages = db.public_pages
            # user_id = data.get("user_info")

            
            found_page = public_pages.find_one(
                {"page_title": serializer.validated_data.get("page_title")}
            )
            if found_page is None:
                #assign it to "designation" key
                default_designations = [
                        {
                            "_id": ObjectId(),
                            "title": "page_admin",
                            "tags": [
                                {
                                    "_id": ObjectId(),
                                    "title": "approval_requests",
                                    "tasks": [
                                        {"_id": ObjectId(), "title": "Approve Join Request", "task_nice_id":"approve_join_request"}
                                    ],
                                },
                                {
                                    "_id": ObjectId(),
                                    "title": "manage_people",
                                    "tasks": [
                                        {"_id": ObjectId(), "title": "Approve Join Request", "task_nice_id":"add_people"},
                                        {"_id": ObjectId(), "title": "Modify Responsibility", "task_nice_id":"modify_responsibility"},
                                        {"_id": ObjectId(), "title": "Suspend user association", "task_nice_id":"suspend_association"}
                                    ],
                                },
                                {
                                    "_id": ObjectId(),
                                    "title": "manage_class",
                                    "tasks": [
                                        {"_id": ObjectId(), "title": "Suspend user association", "task_nice_id":"take_attendance"}
                                    ],
                                },
                                {
                                    "_id": ObjectId(),
                                    "title": "analysis",
                                    "tasks": [
                                        {"_id": ObjectId(), "title": "Student attendance analysis", "task_nice_id":"student_attendance_analysis"}
                                    ],
                                }
                            ],
                        },
                        {
                            "_id": ObjectId(),
                            "title": "Teacher",
                            "tags": [
                                {
                                    "_id": ObjectId(),
                                    "title": "manage_class",
                                    "tasks": [
                                        {"_id": ObjectId(), "title": "Suspend user association", "task_nice_id":"take_attendance"}
                                    ],
                                }
                            ],
                        },
                        {
                            "_id": ObjectId(),
                            "title": "Guardian",
                            "tags": [
                                {
                                    "_id": ObjectId(),
                                    "title": "manage_attendance",
                                    "tasks": [
                                        {"_id": ObjectId(), "title": "Child Attendance Analysis", "task_nice_id":"attendance_analysis"}
                                    ],
                                }
                            ],
                        }
                    ]
            
                serializer.validated_data["designation"] = default_designations
                post_id = public_pages.insert_one(serializer.validated_data).inserted_id
                self.response = {
                    "status_code": "page_creation_successfull",
                    "default_description": "successfully created page",
                    "id": str(post_id),
                }
            else:
                self.response = {
                    "status_code": "registration_failed",
                    "default_description": "already exist",
                    "id": str(found_page["_id"]),
                }
        else:
            self.response = {"error": serializer.errors}


class PublicPageSerializer(serializers.Serializer):
    page_title = serializers.CharField()
    type_of_institute = serializers.CharField()
    founding_date = serializers.CharField()
    address_district = serializers.CharField()
    address_upozila = serializers.CharField()
    no_of_stakeholder = serializers.CharField()
    description = serializers.CharField()
