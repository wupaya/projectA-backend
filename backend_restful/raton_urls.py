from django.conf.urls import url
from .jabin_view import RatonView

urlpatterns = [
    url(r'^raton/$', RatonView.as_view(), name='raton'),
 ]