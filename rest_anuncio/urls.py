from django.urls import path
from .views import lista_Anuncio,detalle_anuncio
from rest_anuncio.viewsLogin import login

urlpatterns = [
     path('listar/',lista_Anuncio,name="Listar"),
     path('detalleanuncio/<id>',detalle_anuncio,name='detalle_anuncio'),
     path('login/',login,name="login"),
     

]