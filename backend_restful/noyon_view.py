from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .noyon import Noyon
from .noyon import Noyon2
from .noyon import Noyon3
from .noyon import Noyon4
from .noyon import Noyon5
from .noyon import NoyonIO
from .noyon import User
from .noyon_serializer import NoyonSerializer
from .noyon_serializer import Noyon2Serializer
from .noyon_serializer import Noyon3Serializer
from .noyon_serializer import Noyon4Serializer
from .noyon_serializer import Noyon5Serializer
from .noyon_serializer import NoyonParameterInput
from .noyon_serializer import NoyonParameterOutput
from .noyon_serializer import RegistrationSerializer

class NoyonView(APIView):
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
        serializer = NoyonSerializer(Noyon())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = NoyonSerializer(Noyon())
        return Response (serializer.data, status.HTTP_200_OK)
        
class Noyon2View(APIView):
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
        serializer = Noyon2Serializer(Noyon2())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Noyon2Serializer(Noyon2())
        return Response (serializer.data, status.HTTP_200_OK)
        
class Noyon3View(APIView):
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
        serializer = Noyon3Serializer(Noyon3())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Noyon3Serializer(Noyon3())
        return Response (serializer.data, status.HTTP_200_OK)

class Noyon4View(APIView):
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
        serializer = Noyon4Serializer(Noyon4())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Noyon4Serializer(Noyon4())
        return Response (serializer.data, status.HTTP_200_OK)
        
class Noyon5View(APIView):
    '''
    **Show Noyon5View**
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
        **Content:** `{ error : "Noyon5View" }`

      OR

      * **Code:** 422 UNPROCESSABLE ENTRY <br />
        **Content:** `{ error : "Can't Connect to server" }`

    * **Sample Call:**

      <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._> 

    * **Notes:**

      <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._> 
    '''
    def get(self,request):
        serializer = Noyon5Serializer(Noyon5())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Noyon5Serializer(Noyon5())
        return Response (serializer.data, status.HTTP_200_OK)
        
class NoyonParamView(APIView):
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
        return Response ({"Message":your_message}, status.HTTP_200_OK)
    def post(self, request, your_message):
        return Response ({"Message":your_message}, status.HTTP_200_OK)
        
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
            user = User()
    
    
    
    '''need password'''
    pass

class PublicPages(APIView):
    '''need password'''
    pass
