from django.urls import path
from .views import Inicio, Listar,SobreNosotros,Contactanos,SistemaCC,TipoCC,Estado,Listar,formularioparche,modificarParche,eliminarparche

urlpatterns = [
     path('', Inicio,name="Inicio"),
     path('Sobre/',SobreNosotros,name="Sobre"),
     path('Contacto/', Contactanos,name="Contacto"),
     path('Sistema/',SistemaCC,name="Sistema"),
     path('Tipo/', TipoCC,name="Tipo"),
     path('Estado/',Estado,name="Estado"),
     path('ListarSql/',Listar,name="ListarSql"),
     path('formularioparche/',formularioparche,name="formularioparche"),
     path('modificarparche/<id>',modificarParche,name="modificarParche"),
     path('eliminarparche/<id>',eliminarparche,name="eliminarparche"),
]