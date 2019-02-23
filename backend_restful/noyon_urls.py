from django.conf.urls import url
from rest_framework import routers
from .views import SignUpView, SubView

from .noyon_view import NoyonView
#use router if you don't want to make url using regular expression like urlpatterns
router = routers.DefaultRouter(trailing_slash = False)



urlpatterns = [
     url(r'^noyon/$', NoyonView.as_view(), name='noyon'), #just using response method  
]
