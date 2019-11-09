from backend_restful.db import users

class manage_request_tag:
    response = {}
    def __init__(self, data={}):
        #query database for dashboard info
        
        
        query_result = {
            "tasks":[
            {"taskid":3, "task_nice_id":"ins_stuff_list","task_description":"Show all stuff"},
            {"taskid":4, "task_nice_id":"ins_add_stuff","task_description":"add new stuff"},
            {"taskid":13, "task_nice_id":"ins_remove_stuff","task_description":"remove stuff"},
            {"taskid":15, "task_nice_id":"ins_stuff_details","task_description":"Show stuff details"},
            {"taskid":16, "task_nice_id":"ins_edit_stuff","task_description":"I want to change the responsibility & permission of stuff"}

            ]
        }

        self.response=query_result