from django.conf.urls import url
from .noyon_view import NoyonView

urlpatterns = [
    url(r'^noyon/$', NoyonView.as_view(), name='noyon'),
]