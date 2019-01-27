from django.conf.urls import url
from rest_framework import routers
from .views import SignUpView

#use router if you don't want to make url using regular expression like urlpatterns
router = routers.DefaultRouter(trailing_slash = False)



urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='signup'), #just using response method
]