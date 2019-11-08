import importlib

mongodb_url = "mongodb+srv://anamika:1234@cluster0-t3qae.mongodb.net/test?retryWrites=true"

class Process:
    response = {}
    def __init__(self, data={}):
        task = data.get("task_id")
        pkg = 'backend_restful.'+"education.tasks"+'.'+task
        tdata = data.get("data")
        #loading task handler module dynamically
        task_handler_object = getattr(importlib.import_module(pkg), task)
        self.response=task_handler_object(task).response



