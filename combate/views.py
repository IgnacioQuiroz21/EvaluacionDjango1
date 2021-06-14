from django.shortcuts import  render,redirect
from .models import Parche
from .forms import ParcheForm

# Create your views here.
def Inicio(request):
    actua={"nombre":"Actualizacion 15/04","descripcion":"Conoce detalles de la actualizacion."}
    
    return render(request,'combate\index.html',actua)

def SobreNosotros(request):
    return render(request,'combate\SobreNosotros.html')

def Contactanos(request):
    return render(request,'combate\Contactanos.html')    

def SistemaCC(request):
    return render(request,'combate\SistemaCC.html')

def TipoCC(request):
    return render(request,'combate\TipoCC.html')

def Estado(request):
    return render(request,'combate\Estado.html')        

def Listar(request):
    listaParches = Parche.objects.all()
    datos = {
        'Parches':listaParches
    }
    return render(request,'combate\Listar.html',datos)


def formularioparche(request):
    datos = {
        'form': ParcheForm()
    }

    if(request.method == 'POST'):
        formulario = ParcheForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'
    return  render(request,'combate\FormularioParche.html',datos)

def modificarParche(request, id):
        parche = Parche.objects.get(idParche=id)

        datos = { 
            'form':ParcheForm(instance=parche)
        }
        
        if(request.method == 'POST'):
            formulario = ParcheForm(data=request.POST, instance=parche)
            if formulario.is_valid():
               formulario.save()
               datos['mensaje'] = 'Guardados correctamente'
        return render(request,'combate\ModificarParche.html',datos)



def eliminarparche(request,id):
    parche = Parche.objects.get(idParche=id)
    parche.delete()
    return redirect(to='Listar')