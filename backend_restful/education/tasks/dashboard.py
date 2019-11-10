from backend_restful.db import users

class dashboard:
    response = {}
    def __init__(self, data={}):
        #query database for dashboard info
        #str(users.find_one({"$and":[{"email": "mhsn06@gmail.com"},{"password": "1234"}]}))
        
        query_result = { 
            "associated": [
            {"id": 1, "short_name":"BRUR", "long_name":"Begum Rokeya University, Rangpur", "designation":"Parent",
            "status": "joined",
            "join_date": "July 1st 2019",
            "allowed_services": [
            { "id": 1, "designation": "Parent" },
            { "id": 2, "designation": "Teacher" } ]},
            {"id": 2, "short_name":"RGC", "long_name":"Rangpur Government College, Rangpur", "designation":"Parent",
            "status": "joined",
            "join_date": "July 1st 2019",
            "allowed_services": [
            { "id": 1, "designation": "Parent" },
            { "id": 2, "designation": "Teacher" } ]},
            ]
        }

        self.response=query_result