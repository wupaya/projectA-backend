from django.conf.urls import url
from .noyon_view import NoyonView
from .noyon_view import Noyon2View
from .noyon_view import Noyon3View
from .noyon_view import Noyon4View
from .noyon_view import Noyon5View
from .noyon_view import NoyonParamView
from .noyon_view import NoyonIOView
from .noyon_view import Search
from .noyon_view import Login
from .noyon_view import Registration
from .noyon_view import PublicPages

urlpatterns = [
    url(r'^noyon/$', NoyonView.as_view(), name='noyon'),
    url(r'^noyon2/$', Noyon2View.as_view(), name='noyon2'),
    url(r'^noyon3/$', Noyon3View.as_view(), name='noyon3'),
    url(r'^noyon4/$', Noyon4View.as_view(), name='noyon4'),
    url(r'^noyon5/$', Noyon5View.as_view(), name='noyon5'),
    url(r'^noyonio/$', NoyonIOView.as_view(), name='noyonio'),  
    url(r'^message/(?P<your_message>.*)/$', NoyonParamView.as_view(), name='message'),
]