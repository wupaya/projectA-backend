from django.conf.urls import url
from .jabin_view import JabinView,JabinView2

urlpatterns = [
    url(r'^jabin/$', JabinView.as_view(), name='jabin'),
    url(r'^jabin2/$', JabinView2.as_view(), name='jabin2'),
 ]