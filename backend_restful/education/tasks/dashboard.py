from backend_restful.db import users

class dashboard:
    response = {}
    def __init__(self, data={}):
        #query database for dashboard info
        
        
        query_result = { 
            "associated": [
            {"id": 1, "short_name":str(users.find_one({"$and":[{"email": "mhsn06@gmail.com"},{"password": "1234"}]})), "long_name":"Begum Rokeya University, Rangpur", "designation":"Parent"},
            {"id": 2, "short_name":"RGC", "long_name":"Rangpur Government College, Rangpur", "designation":"Parent"},
            ]
        }

        self.response=query_result