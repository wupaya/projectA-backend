from django.conf.urls import url
from rest_framework import routers
from .views import HelloView, Hello2View, NiceUrlParamView, ValidateParamView

#use router if you don't want to make url using regular expression like urlpatterns
router = routers.DefaultRouter(trailing_slash = False)



urlpatterns = [
    url(r'hello', HelloView.as_view()), #using serializer
    url(r'hella', Hello2View.as_view()), #just using response method
    url(r'^abc/(?P<pk>\d+)/$', NiceUrlParamView.as_view()), #just using response method
    url(r'^param/$', ValidateParamView.as_view()), #just using response method
]