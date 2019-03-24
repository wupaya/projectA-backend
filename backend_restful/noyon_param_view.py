from django.http import HttpResponse

def noyon_parameter_view(request, name):
    return HttpResponse('<h1>This is Parameter View.</h1><br/>My name is {}'.format(name))