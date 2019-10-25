from django.conf.urls import url
from .view_1 import register, login, public_page, service_details, service_task, service_tag

urlpatterns = [
    url(r'^register/$', register.as_view(), name='register'),
    url(r'^login/$', login.as_view(), name='login'),
    url(r'^public_page/$', public_page.as_view(), name='public_page'),
    url(r'^service_details/$', service_details.as_view(), name='service_details'),
    url(r'^service_task/$', service_task.as_view(), name='service_task'),
    url(r'^service_tag/$', service_tag.as_view(), name='service_tag'),
]
