from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer_1 import RegistrationSerializer, LoginInputSerializer, PublicPageSerializer, ServicesSerializer, ServiceRequestSerializer
from .noyon import AvailableServices, SubscribedServices, PublicPage, ServiceRequest

import pymongo
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import json
from bson import json_util
import jwt
from datetime import datetime
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from django.utils.translation import gettext_lazy as _
import importlib


mongodb_url = "mongodb+srv://anamika:1234@cluster0-t3qae.mongodb.net/test?retryWrites=true"
jwt_secret = "secret"

class login(APIView):
    '''
    **Handle user authentication**
    ----
      user will provide email and password and get a session token on match

    * **URL**

      /login

    * **Method:**

      `POST`

    *  **URL Params**

       no ulr params

    * **Data Params**

    **Required:**

       `email=[string]`
       `password=[string]`

    * **Success Response:**

      * **status_code:** login_successfull <br />
      * **default_description:** successfully registered <br />
        **data:** `{'token': b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiNWQ1YWU0MjExMzYxNGI0ZjcxODU2ZmQ5Iiwic2Vzc2lvbl9pZCI6IjVkNjBiYzE2Zjc1ZjhkZjcxYzQxYmE2YSJ9.ngxcHBHQ9NZQlIT9VKRgUEuGxiyvBl-WRRr7N2sKjYg'}`

    * **Error Response:**

        **status_code:** login_failed <br />
            **default_description:** user not found

    * **Sample Call:**

      ```javascript
    $.ajax({
        url: "/login",
        dataType: "json",
        type : "POST",
        contentType: 'application/json',
        data: JSON.stringify( { "email": "mhsn06@gmail.com", "password": "1234" }),
        success : function(r) {
            console.log(r);
        }
    });
    ```

    * **Notes:**

      It's still under development
    '''
    # def get(self,request):
        # validate request data with serializer

        # query database

        # return error if not found

        # return token

        # return Response (serializer.data, status.HTTP_200_OK)

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
            import pymongo
            if(found_user is not None):


                session_object = {
                    "user": str(found_user),
                    "expired_datetime" : datetime.utcnow()
                }
                sessions = db.sessions
                session = sessions.insert_one(session_object)

                jwt_payload = {'user': str(found_user["_id"]),
                'session_id':str(session.inserted_id)}
                login_object = {"token": jwt.encode(jwt_payload, jwt_secret, algorithm='HS256')}
                return Response({"status_code":"login_successfull",
    "default_description":"successfully registered", "data": login_object}, status=status.HTTP_201_CREATED)
            else:
                return Response({"status_code":"login_failed",
    "default_description":"user not found"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class services(APIView):
    '''
    **Show Noyon2View**
    ----
      <_Additional information about your API call. Try to use verbs that match both request type (fetching vs modifying) and plurality (one vs multiple)._>

    * **URL**

      <_The URL Structure (path only, no root url)_>

    * **Method:**

      <_The request type_>

      `GET` | `POST` | `HEAD` | `OPTIONS`

    *  **URL Params**

       <_If URL params exist, specify them in accordance with name mentioned in URL section. Separate into optional and required. Document data constraints._>

       **Required:**

       `id=[integer]`

       **Optional:**

       `photo_id=[alphanumeric]`

    * **Data Params**

      <_If making a post request, what should the body payload look like? URL Params rules apply here too._>

    * **Success Response:**

      <_What should the status code be on success and is there any returned data? This is useful when people need to to know what their callbacks should expect!_>

      * **Code:** 200 <br />
        **Content:** `{ id : 12 }`

    * **Error Response:**

      <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

      * **Code:** 401 UNAUTHORIZED <br />
        **Content:** `{ error : "Noyon2View" }`

      OR

      * **Code:** 422 UNPROCESSABLE ENTRY <br />
        **Content:** `{ error : "Can't Connect to server" }`

    * **Sample Call:**

      <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._>

    * **Notes:**

      <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._>
    '''
    def get(self,request):
        #query database

        #return a list of services

        serializer = Noyon2Serializer(Noyon2())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Noyon2Serializer(Noyon2())
        return Response (serializer.data, status.HTTP_200_OK)

class register(APIView):
    '''
    **Register New User**
    ----
      Register a user

    * **URL**

      /register

    * **Method:**

      `POST`

    * **URL Params**

       No Params


    * **Data Params**

        `email=string`

        `password=string`

        `name=string`

        `phone_no=string`


    * **Success Response:**


      * **status_code:** registration_successfull <br />
        **default_description:** `successfully registered`
        **id:** `5d60ce0ee8dc7a242d323337`

    * **Error Response:**

      * **status_code:** registration_failed <br />
        **default_description:** `already registered`
        **id:** `5d60ce0ee8dc7a242d323337`

    * **Sample Call:**

      ```javascript
    $.ajax({
        url: "/register",
        dataType: "json",
        type : "POST",
        contentType: 'application/json',
        data: JSON.stringify( { "email": "mhsn06@gmail.com", "password": "1234","name":"hassan", "phone_no":"01737343005" }),
        success : function(r) {
            console.log(r);
        }
    });
    ```

    * **Notes:**

      It's still under development.
    '''

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
    '''
    **Show Noyon4View**
    ----
      <_Additional information about your API call. Try to use verbs that match both request type (fetching vs modifying) and plurality (one vs multiple)._>

    * **URL**

      <_The URL Structure (path only, no root url)_>

    * **Method:**

      <_The request type_>

      `GET` | `POST` | `HEAD` | `OPTIONS`

    *  **URL Params**

       <_If URL params exist, specify them in accordance with name mentioned in URL section. Separate into optional and required. Document data constraints._>

       **Required:**

       `id=[integer]`

       **Optional:**

       `photo_id=[alphanumeric]`

    * **Data Params**

      <_If making a post request, what should the body payload look like? URL Params rules apply here too._>

    * **Success Response:**

      <_What should the status code be on success and is there any returned data? This is useful when people need to to know what their callbacks should expect!_>

      * **Code:** 200 <br />
        **Content:** `{ id : 12 }`

    * **Error Response:**

      <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

      * **Code:** 401 UNAUTHORIZED <br />
        **Content:** `{ error : "Noyon4View" }`

      OR

      * **Code:** 422 UNPROCESSABLE ENTRY <br />
        **Content:** `{ error : "Can't Connect to server" }`

    * **Sample Call:**

      <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._>

    * **Notes:**

      <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._>
    '''

    def post(self, request):

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
            return Response(task_handler_object(task).response, status.HTTP_200_OK)
          except Exception as e:
            return Response({"error": str(e)}, status.HTTP_200_OK)
        return Response (serializer.errors, status.HTTP_200_OK)

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('Authorization')
        print(token)
        # if not username:
            # return None
        try:
            user = User.objects.get()
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        return (user, None)


class TokenAuthentication(authentication.BaseAuthentication):
    """
    Simple token based authentication.
    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:
        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = 'Token'
    model = None

    def get_authorization_header(self, request):
        """
        Return request's 'Authorization:' header, as a bytestring.
        Hide some test client ickyness where the header can be unicode.
        """
        auth = request.META.get('HTTP_AUTHORIZATION', b'')
        if isinstance(auth, str):
            # Work around django test client oddness
            auth = auth.encode(HTTP_HEADER_ENCODING)
        return auth

    def get_model(self):
        if self.model is not None:
            return self.model
        from rest_framework.authtoken.models import Token
        print(Token)
        return Token

    """
    A custom token model may be used, but must have the following properties.
    * key -- The string identifying the token
    * user -- The user to which the token belongs
    """

    def authenticate(self, request):
        auth = self.get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1]
        except Exception as e:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            #token = model.objects.select_related('user').get(key=key)
            token = jwt.decode(key, jwt_secret, algorithms=['HS256'])
            user = User.objects.get()
        except Exception as e:
            print(Exception)
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        # if not token.user.is_active:
            # raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
        return (user, token)

    def authenticate_header(self, request):
        return self.keyword

class public_page(APIView):
    '''
    **Public Page**
    ----
      Register and manage public page

    * **URL**

      /public_page

    * **Method:**

      `POST`

    *  **URL Params**

       No Params

    * **Data Params**

      `page_title=string`
      `type_of_institute=string`
      `founding_date=string`
      `address_district=string`
      `address_upozila=string`
      `no_of_stakeholder=string`
      `description=string`

    * **Success Response:**

      * **status_code:** page_creation_successfull
      * **default_description:** successfully created page
        **id:** `5d60d59ff0626c6be06ec94c`

    * **Error Response:**

      * **status_code:** registration_failed <br />
        **default_description:** `already exist`
        **id:** `5d5beb87fe6518dd9565243b`

    * **Sample Call:**

      ```javascript
    $.ajax({
        url: "/public_page",
        dataType: "json",
        type : "POST",
        contentType: 'application/json',
        data: JSON.stringify( {
            "page_title":"begum rokeya university, rangpur",
            "type_of_institute": "university",
            "founding_date":"2008",
            "address_district":"rangpur",
            "address_upozila":"sadar",
            "no_of_stakeholder":"20",
            "description":"this is a test page"
        }),
        success : function(r) {
            console.log(r);
        }
    });
    ```

    * **Notes:**

      Requires authentication
    '''


    authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    # def get(self,request, your_message):
        #validate pageid with serializer

        #query database for page information

        #return error if not found

        #return details
        # return Response ({"Message":your_message}, status.HTTP_200_OK)
    def get(self, request):
        serializer = PublicPageSerializer(PublicPage())
        return Response (serializer.data, status.HTTP_200_OK)

    def post(self, request, format=None):
        #validate page create data
        serializer = PublicPageSerializer(data=request.data)

        #get user from session_id
        #get
        #store the data in database
        if serializer.is_valid():
            #serializer data for database
            #database instance
            client = pymongo.MongoClient(mongodb_url)
            db = client.test
            public_pages = db.public_pages

            #query if already exist
            found_page = public_pages.find_one({"page_title": serializer.validated_data.get("page_title")})
            if(found_page is None):
                post_id = public_pages.insert_one(serializer.validated_data).inserted_id

                return Response({"status_code":"page_creation_successfull",
    "default_description":"successfully created page", "id": str(post_id)}, status=status.HTTP_200_OK)
            else:
                return Response({"status_code":"registration_failed",
    "default_description":"already exist", "id": str(found_page["_id"])}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        #return status message


class NoyonIOView(APIView):
    def get(self,request):
        #serializer = NoyonParameterInput(data=request.data)
        #if serializer.is_valid():

        num1 = request.query_params.get('num1', None)
        num2 = request.query_params.get('num2', None)
        nio = NoyonIO.give_me_sum(num1,num2)
        if num1 is not None and num1.isnumeric() and num2 is not None and num2.isnumeric():
            #nio = NoyonIO.filter(give_me_sum(int(num1),int(num2))
            nio = nio.filter(num1+num2)
        return nio

    def post(self,request):
        serializer = NoyonParameterInput(data=request.data)
        if serializer.is_valid():
            nio = NoyonIO()
            nio.sum = nio.give_me_sum(serializer.validated_data.get('num1'),serializer.validated_data.get('num2'))
            return Response(NoyonParameterOutput(nio).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Search(APIView):
    '''need password'''
    pass

class Login(APIView):
    '''need password'''
    pass

class Registration(APIView):
    def get(self, request):
        serializer = RegistrationSerializer(data=request.data)
        user = User()
        #suppose u read the following data from database and u assign them to the user object
        user.email = "example@domain.com"
        user.password = "password12@#"
        user.username = "name123"
        user.name = "Mr. Name"
        user.phone_no = "+1847439202"
        return Response(RegistrationSerializer(user).data, status=status.HTTP_201_CREATED)

    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            #user = User()
            #TODO store data in database
            return Response ({"Registratiion Successfull"}, status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    '''need password'''
    pass

class services(APIView):
    def get(self,request):
        availableService = [AvailableServices(id = '1', title = 'Available Service 1', description = 'Service description 1'),
                            AvailableServices(id = '2', title = 'Available Service 2', description = 'Service description 2'),
                            AvailableServices(id = '3', title = 'Available Service 3', description = 'Service description 3'),
                            AvailableServices(id = '4', title = 'Available Service 4', description = 'Service description 4')]
        available_serializer = ServicesSerializer(availableService, many=True)

        subscribedService = [SubscribedServices(id = '1', title = 'Subscribed Service 1', description = 'Service description 1'),
                            SubscribedServices(id = '2', title = 'Subscribed Service 2', description = 'Service description 2'),
                            SubscribedServices(id = '3', title = 'Subscribed Service 3', description = 'Service description 3'),
                            SubscribedServices(id = '4', title = 'Subscribed Service 4', description = 'Service description 4')]
        subscribed_serializer = ServicesSerializer(subscribedService, many=True)
        return Response ({"AvailableServices":available_serializer.data, "SubscribedServices":subscribed_serializer.data}, status.HTTP_200_OK)

    def post(self,request):
        subscribedService = [SubscribedServices(id = '1', title = 'Subscribed Service 1', description = 'Service description 1'),
                            SubscribedServices(id = '2', title = 'Subscribed Service 2', description = 'Service description 2'),
                            SubscribedServices(id = '3', title = 'Subscribed Service 3', description = 'Service description 3'),
                            SubscribedServices(id = '4', title = 'Subscribed Service 4', description = 'Service description 4')]
        subscribed_serializer = ServicesSerializer(subscribedService, many=True)
        #serializer data for database
        #database instance
        client = pymongo.MongoClient(mongodb_url)
        db = client.test
        subscribed_services = db.subscribed_services
        #just inserting the first data for testing
        first_data = subscribed_serializer.data[0]
        found_subscribed_services = subscribed_services.find_one({"id": first_data.get("id"), "title": first_data.get("title"), "description":first_data.get("description")})
        if(found_subscribed_services is None):
            post_id = subscribed_services.insert_one(first_data).inserted_id
            return Response({"status_code":"subscribed_services_added_successfull",
"default_description":"successfully added the subscribed servics", "id": str(post_id)}, status=status.HTTP_200_OK)
        else:
            return Response({"status_code":"Subscribed_ervices_failed",
"default_description":"already exist", "id": str(found_subscribed_services["_id"])}, status=status.HTTP_200_OK)
        return Response(subscribed_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
