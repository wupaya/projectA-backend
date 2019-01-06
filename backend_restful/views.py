from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_world(*args, **kwargs):
	return HttpResponse("Hello World")
	
def hello_world2(*args, **kwargs):
	return HttpResponse("<h1>Hello World 2</br>From Branch hw_2</h2>")