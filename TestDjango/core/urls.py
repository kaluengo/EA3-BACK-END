from django.urls import path
from .views import form_contacto

urlpatterns = [
    path('',home, name="home"),
    path('',inicio,name= "inicio")
]



