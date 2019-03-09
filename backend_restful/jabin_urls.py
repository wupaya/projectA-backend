from django.conf.urls import url
from .jabin_view import JabinView

urlpatterns = [
    url(r'^jabin/$', JabinView.as_view(), name='jabin'),
 ]