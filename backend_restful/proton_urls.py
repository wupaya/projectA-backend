from django.conf.urls import url
from .proton_view import ProtonView
from .proton_view import Proton2View
from .proton_view import Proton3View
from .proton_view import Proton4View
from .proton_view import proton5View

urlpatterns = [
    url(r'^proton/$', ProtonView.as_view(), name='proton'),
    url(r'^proton2/$', Proton2View.as_view(), name='proton2'),
    url(r'^proton3/$', Proton3View.as_view(), name='proton3'),
    url(r'^proton4/$', Proton4View.as_view(), name='proton4'),
    url(r'^proton5/$', proton5View.as_view(), name='proton5'),
]