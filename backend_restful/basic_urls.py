from django.conf.urls import url
from .view_1 import register, login, public_page, services

urlpatterns = [
    url(r'^register/$', register.as_view(), name='register'),
    url(r'^login/$', login.as_view(), name='login'),
    url(r'^public_page/$', public_page.as_view(), name='public_page'),
    url(r'^services/$', services.as_view(), name='services'),
]
