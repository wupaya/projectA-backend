class Noyon(object):
    greetings = "Hello, i'm Noyon"

class Noyon2(object):
    greetings = "Hello again, i'm Noyon"

class Noyon3(object):
    greetings = "Hi There, i'm Noyon"

class Noyon4(object):
    greetings = "Hey, i'm Noyon, What's up?"

class Noyon5(object):
    greetings = "Hey, i'm Noyon, How can i help you?"

class NoyonIO(object):
    sum = ""
    def give_me_sum(num1,num2):
        return num1+num2

class User(object):
    email = ""
    password = ""
    user_name = ""
    user_id = ""
    name = ""
    phone_no = ""

class Registration(object):
    user_id = ""
    registration_date = ""
    email_activation_status = ""

class PublicPage(object):
    page_title = "Page Title here"
    type_of_institute = "Type of Institue Here"
    founding_date = "founding date here"
    address_district = "district address here"
    address_upozila = "Upozilla address here"
    no_of_stakeholder = "Number of Stakeholder here"
    description = "Page description here"

class Session(object):
    ueer_id = ""
    session_id = ""
    expired_date_time = ""

class AvailableServices(object):
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

class SubscribedServices(object):
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        
class ServiceRequest(object):
    service_name = "This is a service name"
    task_name = "This is a task name"
    data = "This is a data"
