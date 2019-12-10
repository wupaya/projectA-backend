from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer_1 import RegistrationSerializer, LoginInputSerializer, PublicPageSerializer, ServicesSerializer, ServiceRequestSerializer
from .noyon import AvailableServices, SubscribedServices, PublicPage, ServiceRequest
import pymongo
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from bson import json_util
import jwt, json
from datetime import datetime
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from django.utils.translation import gettext_lazy as _
import importlib
from pprint import pprint
from bson.objectid import ObjectId
from .helper import IsGetOrIsAuthenticated, TokenAuthentication, ExampleAuthentication

mongodb_url = "mongodb+srv://anamika:1234@cluster0-t3qae.mongodb.net/test?retryWrites=true"
jwt_secret = "secret"

class login(APIView):

    def post(self, request, format=None):
        #validate input data with serializer
        serializer = LoginInputSerializer(data=request.data)
        #store in database
        if serializer.is_valid():
            #serializer data for database
            #database instance
            client = pymongo.MongoClient(mongodb_url)
            db = client.test
            users = db.users

            #query if already exist
            found_user = users.find_one(
              {"$and":[
                {"email": serializer.validated_data.get("email")},
                {"password": serializer.validated_data.get("password")}
              ]},
              {
                "subscribed_services":1,
                "_id":1,
                "recent_tasks": 1
              }
            )
            if(found_user is not None):
                session_object = {
                    "user": str(found_user),
                    "expired_datetime" : datetime.utcnow()
                }
                sessions = db.sessions
                session = sessions.insert_one(session_object)

                jwt_payload = {'user': str(found_user["_id"]),
                'session_id':str(session.inserted_id)}
                login_object = {
                  "token": jwt.encode(jwt_payload, jwt_secret, algorithm='HS256'),
                  "subscribed_services" : found_user.get("subscribed_services", []),
                  "recent_tasks": found_user.get("recent_tasks", [])
                }
                return Response({"status_code":"login_successfull",
    "default_description":"Login Successfull", "data": login_object}, status=status.HTTP_201_CREATED)
            else:
                return Response({"status_code":"login_failed",
    "default_description":"user not found"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class register(APIView):
    
    def get(self,request):
        #serializer = Noyon3Serializer(Noyon3())
        return Response ({}, status.HTTP_200_OK)
    def post(self, request, format=None):
        #validate input data with serializer
        serializer = RegistrationSerializer(data=request.data)
        #store in database
        if serializer.is_valid():
            #serializer data for database
            #database instance
            client = pymongo.MongoClient(mongodb_url)
            db = client.test
            users = db.users

            #query if already exist
            found_user = users.find_one({"email": serializer.validated_data.get("email")})
            if(found_user is None):
                post_id = users.insert_one(serializer.validated_data).inserted_id

                return Response({"status_code":"registration_successfull",
    "default_description":"successfully registered", "id": str(post_id)}, status=status.HTTP_201_CREATED)
            else:
                return Response({"status_code":"registration_failed",
    "default_description":"already registered", "id": str(found_user["_id"])}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        #return status

class service_request(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pprint(request.auth["user"])

        #serializing incoming data
        serializer = ServiceRequestSerializer(data=request.data)

        if serializer.is_valid():
          service_name = serializer.validated_data.get("service_name")
          task = serializer.validated_data.get("task")
          pkg = 'backend_restful.'+service_name+'.'+service_name

          #loading task handler module dynamically
          task_handler_object = getattr(importlib.import_module(pkg), "Process")
          
          try:
            #process task and return response
            data = task
            data["user_info"] = request.auth["user"]
            response = task_handler_object(task).response
            #response["user"] = request.auth["user"]
            return Response(response, status.HTTP_200_OK)
          except Exception as e:
            return Response({"error": str(e)}, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_200_OK)

class public_page(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsGetOrIsAuthenticated]

    def get(self, request, pageid=None):
      if pageid is None:
        return Response({"error": "page_id_missing", "details":"page is missing"}, status.HTTP_200_OK)
      public_page_id = pageid
      client = pymongo.MongoClient(mongodb_url)
      db = client.test
      collection = db.public_pages
      
      document = collection.find_one({"_id": ObjectId(public_page_id)})

      if(document is None):
        #return not found error
        return Response({"status_code":"not_found", "default_description":"no such thing exits in the system"}, status=status.HTTP_200_OK)

      document = json.loads(json.dumps(document))
      document["lastest_events"] = [
        { "title": "News: CSE BRUR started using IMS system.", "details_link": "#" },
        { "title": "Event: Inter batch programming contest on sunday, 9th oct.", "details_link": "#" },
        { "title": "Circular: Admission is open", "details_link": "#" },
        { "title": "Notice: New Policy for Scholarship.", "details_link": "#" }
      ]

      return Response(document, status.HTTP_200_OK)

    def post(self, request, format=None):
      #validate page create data
      serializer = PublicPageSerializer(data=request.data)

      #store the data in database
      if serializer.is_valid():
          page_type = serializer.validated_data.get("page_type") #education
          pkg = 'backend_restful.'+page_type+'.'+page_type

          #loading task handler module dynamically
          task_handler_object = getattr(importlib.import_module(pkg), "Process")
          task= {
                "task_id": "create_public_page",
                "data": serializer.validated_data
          }
          # try:
          #process task and return response
          data = task
          data["user_info"] = request.auth["user"]
          response = task_handler_object(task).response
          return Response(response, status.HTTP_200_OK)
          # except Exception as e:
          #   return Response({"error": str(e)}, status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Search(APIView):
    '''need password'''
    pass

class services(APIView):
    #imposing authentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):

        #defining static available services
        availableService = [
          AvailableServices(id = '1', title = 'Available Service 1', description = 'Service description 1'),
          AvailableServices(id = '2', title = 'Available Service 2', description = 'Service description 2'),
          AvailableServices(id = '3', title = 'Available Service 3', description = 'Service description 3'),
          AvailableServices(id = '4', title = 'Available Service 4', description = 'Service description 4')
        ]

        #serializing for response
        available_serializer = ServicesSerializer(availableService, many=True)
        
        #query user for subscribed services
        user_id = request.auth["user"]
        client = pymongo.MongoClient(mongodb_url)
        db = client.test
        users = db.users

        #query if already exist
        found_user = users.find_one({"_id":user_id}, {"subscribed_services":1})

        subscribedService = [
          SubscribedServices(id = '1', title = 'Subscribed Service 1', description = 'Service description 1'),
          SubscribedServices(id = '2', title = 'Subscribed Service 2', description = 'Service description 2'),
          SubscribedServices(id = '3', title = 'Subscribed Service 3', description = 'Service description 3'),
          SubscribedServices(id = '4', title = 'Subscribed Service 4', description = 'Service description 4')
        ]
        subscribed_serializer = ServicesSerializer(subscribedService, many=True)
        
        return Response ({"AvailableServices":available_serializer.data, "SubscribedServices":found_user}, status.HTTP_200_OK)

    def post(self,request):
        subscribedService = [
          SubscribedServices(id = 1, title = 'Education', description = 'Service description 1'),
          SubscribedServices(id = 2, title = 'Health', description = 'Service description 2'),
          SubscribedServices(id = 3, title = 'Business', description = 'Service description 3'),
          SubscribedServices(id = 4, title = 'Propritory', description = 'Service description 4')
        ]
        subscribed_serializer = ServicesSerializer(subscribedService, many=True)
        #serializer data for database
        #database instance
        user_id = request.auth["user"]
        pprint(user_id)
        client = pymongo.MongoClient(mongodb_url)
        db = client.test
        users = db.users
        
        #if subscribed_serializer.is_valid():
        #print("valid")
        #print("user id: " + user_id)
        res = users.update_one({"_id":ObjectId(user_id)}, {"$set": {"subscribed_services":subscribed_serializer.data}}, upsert=False)

        #client = pymongo.MongoClient(mongodb_url)
        #db = client.test
        #subscribed_services = db.subscribed_services
        
        #just inserting the first data for testing
        #first_data = subscribed_serializer.data[0]
        #found_subscribed_services = subscribed_services.find_one({"id": first_data.get("id"), "title": first_data.get("title"), "description":first_data.get("description")})
        if(res.matched_count > 0):
            #post_id = subscribed_services.insert_one(first_data).inserted_id
            return Response({"status_code":"subscribed_services_added_successfull", "default_description":"successfully added the subscribed servics", "id": str(1)}, status=status.HTTP_200_OK)
        else:
            return Response({"status_code":"Subscribed_ervices_failed", "default_description":"already exist", "id": str()}, status=status.HTTP_200_OK)
        return Response(subscribed_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
