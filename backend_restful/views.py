from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer, HelloParamSerializer, HelloMessageSerializer, SignUpInputDataSerializer
from .my_app import Hello, HelloParam
	
	
class Hello2View(APIView):
     '''
	 simple use of response no serialization
	 '''
     def get(self, request):
        return Response({"hello":"world"})
		
class HelloView(APIView):
    '''
	simple use of serialization
	'''
    def get(self, request, pk=None):
        hello = Hello(name=request.query_params.get('name'))
        serializer = HelloSerializer(hello)
        return Response(serializer.data)
		
class NiceUrlParamView(APIView):
     '''
	 simple use of nice url parameters
	 '''
     def get(self, request, pk=None):
        return Response({"pk":pk})		
		
class ValidateParamView(APIView):
    '''
    **Show User**
    ----
      Returns json data about a single user.

    * **URL**
      
        /users/:id

    * **Method:**

        `GET`
      
    *  **URL Params**

        **Required:**
     
        `id=[integer]`

    * **Data Params**

        None

    * **Success Response:**

        * **Code:** 200 <br />
            **Content:** `{ id : 12, name : "Michael Bloom" }`
     
    * **Error Response:**

        * **Code:** 404 NOT FOUND <br />
            **Content:** `{ error : "User doesn't exist" }`

        OR

        * **Code:** 401 UNAUTHORIZED <br />
            **Content:** `{ error : "You are unauthorized to make this request." }`
    
    * **Sample Call:**

    ```javascript
    $.ajax({
        url: "/users/1",
        dataType: "json",
        type : "GET",
        success : function(r) {
            console.log(r);
        }
    });
    ```
        
    * **Sample Call:**
        ```javascript
        $.ajax({
          url: "/users/1",
          dataType: "json",
          type : "GET",
          success : function(r) {
            console.log(r);
          }
        });
        ```
	'''
    def post(self, request, pk=None):
        serializer = HelloParamSerializer(data=request.data)
        if serializer.is_valid():
          helloparamobject = HelloParam(serializer.validated_data.get('param1'),serializer.validated_data.get('param2'))
          return Response(HelloMessageSerializer(helloparamobject).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		
class SignUpView(APIView):
    '''
    **Title**
    ----
      <_Additional information about your API call. Try to use verbs that match both request type (fetching vs modifying) and plurality (one vs multiple)._>

    * **URL**

      <_The URL Structure (path only, no root url)_>

    * **Method:**
      
      <_The request type_>

      `GET` | `POST` | `DELETE` | `PUT`
      
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
        **Content:** `{ error : "Log in" }`

      OR

      * **Code:** 422 UNPROCESSABLE ENTRY <br />
        **Content:** `{ error : "Email Invalid" }`

    * **Sample Call:**

      <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._> 

    * **Notes:**

      <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._> 
    '''
    def post(self, request):
        sign_up_input_serializer = SignUpInputDataSerializer(data=request.data)
        
        if sign_up_input_serializer.is_valid():
			#process signup data here
            pass
        return Response(sign_up_input_serializer.errors, status.HTTP_400_BAD_REQUEST)