from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer_1 import RegistrationSerializer, LoginInputSerializer, PublicPageSerializer
import pymongo
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import json
from bson import json_util

mongodb_url = "mongodb+srv://anamika:1234@cluster0-t3qae.mongodb.net/test?retryWrites=true"

class login(APIView):
    '''
    **Show NoyonView**
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
        **Content:** `{ error : "NoyonView" }`

      OR

      * **Code:** 422 UNPROCESSABLE ENTRY <br />
        **Content:** `{ error : "Can't Connect to server" }`

    * **Sample Call:**

      <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._> 

    * **Notes:**

      <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._> 
    '''
    def get(self,request):
        #validate request data with serializer
        
        #query database
        
        #return error if not found
        
        #return token
        
        return Response (serializer.data, status.HTTP_200_OK)
    
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
            found_user = users.find_one({"$and":[{"email": serializer.validated_data.get("email")},{"password": serializer.validated_data.get("password")}]})
            if(found_user is not None):
                login_object = {"token": "j2lj3j092j03j2roi3jij",
                "expired":"3-2-2020"}
                sessions = db.sessions
                session = sessions.insert_one(login_object)
                
                return Response({"status_code":"login_successfull",
    "default_description":"successfully registered", "data": str(login_object)}, status=status.HTTP_201_CREATED)
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

class serviece_request(APIView):
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
    def get(self,request):
        #validate request data with serializer
        
        #query database for service
        
        #return error if not found
        
        #call service handler object and pass data
        
        #return service handler response
        
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Noyon4Serializer(Noyon4())
        return Response (serializer.data, status.HTTP_200_OK)
        
class public_page(APIView):
    '''
    **Show NoyonParamView**
    ----
      <_Additional information about your API call. Try to use verbs that match both request type (fetching vs modifying) and plurality (one vs multiple)._>

    * **URL**

      <_The URL Structure (path/message, no root url)_>

    * **Method:**
      
      <_The request type_>

      `GET` | `POST` | `HEAD` | `OPTIONS`
      
    *  **URL Params**

       <_If URL params exist, specify them in accordance with name mentioned in URL section. Separate into optional and required. Document data constraints._> 

       **Required:**
     
       `message=[alphanumeric]`

    * **Data Params**

      <_If making a post request, what should the body payload look like? URL Params rules apply here too._>

    * **Success Response:**
      
      <_What should the status code be on success and is there any returned data? This is useful when people need to to know what their callbacks should expect!_>

      * **Code:** 200 <br />
        **Content:** `{ id : 12 }`
     
    * **Error Response:**

      <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

      * **Code:** 401 UNAUTHORIZED <br />
        **Content:** `{ error : "NoyonParamView" }`

      OR

      * **Code:** 422 UNPROCESSABLE ENTRY <br />
        **Content:** `{ error : "Can't Connect to server" }`

    * **Sample Call:**

      <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._> 

    * **Notes:**

      <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._> 
    '''
    def get(self,request, your_message):
        #validate pageid with serializer
        
        #query database for page information
        
        #return error if not found
        
        #return details
        return Response ({"Message":your_message}, status.HTTP_200_OK)
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

class PublicPages(APIView):
    '''need password'''
    pass
