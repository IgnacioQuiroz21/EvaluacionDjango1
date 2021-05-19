from django.urls import path
from .views import Inicio,SobreNosotros,Contactanos,SistemaCC,TipoCC,Estado

urlpatterns = [
     path('', Inicio,name="Inicio"),
     path('Sobre/',SobreNosotros,name="Sobre"),
     path('Contacto/', Contactanos,name="Contacto"),
     path('Sistema/',SistemaCC,name="Sistema"),
     path('Tipo/', TipoCC,name="Tipo"),
     path('Estado/',Estado,name="Estado"),

]