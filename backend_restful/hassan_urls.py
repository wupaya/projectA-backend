from django.conf.urls import url
from .noyon_view import NoyonView
from .hassan_view import Example



urlpatterns = [
    url(r'^hassan/$', Example.as_view(), name='noyon'),
]