from django.urls import path
from .views import lista_Anuncio

urlpatterns = [
     path('listar/',lista_Anuncio,name="Listar"),
     

]