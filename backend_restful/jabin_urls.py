from django.conf.urls import url
from .jabin_view import JabinView,JabinView2

urlpatterns = [
    url(r'^jabin/$', JabinView.as_view(), name='jabin'),
    url(r'^jabin2/$', JabinView.as_view2(), name='jabin2'),
 ]