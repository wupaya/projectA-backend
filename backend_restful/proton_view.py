from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .proton import Proton
from .proton import Proton2
from .proton import Proton3
from .proton import Proton4
from .proton import Proton5
from .proton_serializer import ProtonSerializer
from .proton_serializer import Proton2Serializer
from .proton_serializer import Proton3Serializer
from .proton_serializer import Proton4Serializer
from .proton_serializer import Proton5Serializer

class ProtonView(APIView): 
   '''
    **Show ProtonView**
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
    def get(self, request):
        serializer = ProtonSerializer(Proton())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = ProtonSerializer(Proton())
        return Response (serializer.data, status.HTTP_200_OK)
        
class Proton2View(APIView):
    def get(self,request):
        serializer = Proton2Serializer(Proton2())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Proton2Serializer(Proton2())
        return Response (serializer.data, status.HTTP_200_OK)
        
class Proton3View(APIView):
    def get(self,request):
        serializer = Proton3Serializer(Proton3())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Proton3Serializer(Proton3())
        return Response (serializer.data, status.HTTP_200_OK)

class Proton4View(APIView):
    def get(self,request):
        serializer = Proton4Serializer(Proton4())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Proton4Serializer(Proton4())
        return Response (serializer.data, status.HTTP_200_OK)
        
class Proton5View(APIView):
    def get(self,request):
        serializer = Proton5Serializer(Proton5())
        return Response (serializer.data, status.HTTP_200_OK)
    def post(self, request):
        serializer = Proton5Serializer(Proton5())
        return Response (serializer.data, status.HTTP_200_OK)
