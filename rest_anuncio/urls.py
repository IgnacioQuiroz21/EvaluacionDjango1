from django.urls import path
from .views import lista_Anuncio,detalle_anuncio

urlpatterns = [
     path('listar/',lista_Anuncio,name="Listar"),
     path('detalleanuncio/<id>',detalle_anuncio,name='detalle_anuncio'),
     

]