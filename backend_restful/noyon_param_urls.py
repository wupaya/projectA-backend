from django.urls import path
from . import noyon_param_view

urlpatterns = [
    path('noyonparam/<name>/', noyon_param_view.noyon_parameter_view),
]
