

class Hello(object):
    def __init__(self, name=None):
        self.greetings = 'Hi ' + str(name)
		
class HelloParam(object):
    def __init__(self, param1, param2):
        self.message = param1 + ' ' + param2