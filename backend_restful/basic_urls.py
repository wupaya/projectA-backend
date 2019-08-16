from django.conf.urls import url
from .view_1 import registrater, login

urlpatterns = [
    url(r'^register/$', registrater.as_view(), name='register'),
    url(r'^login/$', login.as_view(), name='login'),
]