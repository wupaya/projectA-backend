        
class SignupRequest(object):
    user_email = None
    user_full_name = None
    user_sex = None
    user_phone_no = None
    request_created_date = None
    request_is_accepted = None
    request_is_email_verified = None
    request_is_phone_no_verified = None
    
    def __init__(self):
        pass
        
    def accept(self):
        self.isAccepted = True
    
    def reject(self):
        self.isAccepted = False
        
    def process_data(self, data_from_source):
        #do some processing
        return data_from_source
		
class Sub(object):
    num1 = None
    num2 = None
    message = "hello Sub"