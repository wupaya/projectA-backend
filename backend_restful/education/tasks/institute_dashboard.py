from backend_restful.db import users

class institute_dashboard:
    response = {}
    def __init__(self, data={}):
        #query database for dashboard info
        
        
        query_result = {
            "associations": ["Headmaster", "Parent"],
            "designation": "Headmaster",
            "console_tags": [
                { "tag_id": 1, "tag_nice_id": "ins_people", "title": "Manage People", "description": "Manage all of your people here" },
                { "tag_id": 2, "tag_nice_id": "ins_responsibilities", "title": "Manage Responsibility", "description": "Manage the responsibility of people" },
                { "tag_id": 3, "tag_nice_id": "ins_requests", "title": "Manage Requests", "description": "Manage requests for approval" },
                { "tag_id": 4, "tag_nice_id": "ins_analysis", "title": "Manage Analysis", "description": "Manage analysis here" },
            ],
            "next_offset": 5
        }

        self.response=query_result