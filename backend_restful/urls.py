from django.conf.urls import url, include
from rest_framework import routers
from .views import SignUpView, SubView

#use router if you don't want to make url using regular expression like urlpatterns
router = routers.DefaultRouter(trailing_slash = False)



urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='signup'), #just using response method
     url(r'^sub/$', SubView.as_view(), name='sub'), #just using response method
     url(r'^', include('backend_restful.noyon_urls')), #just using response method
    url(r'^', include('backend_restful.hassan_urls')), #just using response method
    url(r'^', include('backend_restful.proton_urls')), #just using response method
]
