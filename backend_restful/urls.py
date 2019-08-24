from django.conf.urls import url, include
from rest_framework import routers
from .views import SignUpView, SubView

#use router if you don't want to make url using regular expression like urlpatterns
router = routers.DefaultRouter(trailing_slash = False)



urlpatterns = [
    # url(r'^', include('backend_restful.noyon_urls')), #just using response method
    # url(r'^', include('backend_restful.hassan_urls')), #just using response method
    # url(r'^', include('backend_restful.proton_urls')), #just using response method
    # url(r'^', include('backend_restful.jabin_urls')), #just using response method
    # url(r'^', include('backend_restful.raton_urls')), #just using response method
    url(r'^', include('backend_restful.basic_urls')), #just using response method
]