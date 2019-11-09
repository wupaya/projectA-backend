from django.conf.urls import url
from .view_1 import register, login, public_page, services, service_request

urlpatterns = [
    url(r'^register/$', register.as_view(), name='register'),
    url(r'^login/$', login.as_view(), name='login'),
    url(r'^public_page/$', public_page.as_view(), name='public_page'),
    url(r'^services/$', services.as_view(), name='services'),
    url(r'^service_request/$', service_request.as_view(), name= 'service_request'),
]
