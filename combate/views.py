from django.shortcuts import  render,redirect
from .models import Anuncio, Parche, Proveedor
from .forms import ParcheForm

# Create your views here.
def Inicio(request):
    ultimoParche=Parche.objects.all().reverse()[0]
    penultimoParche=Parche.objects.all().reverse()[1]
    Proov= Proveedor.objects.get(nombre=ultimoParche.nombre)
    Proov1= Proveedor.objects.get(nombre=penultimoParche.nombre)
    anun1 = Anuncio.objects.all()[0]
    anun2 = Anuncio.objects.all()[1]
    anun3 = Anuncio.objects.all()[2]
    img1 = Proveedor.objects.get(nombre=anun1.nombre)
    img2 = Proveedor.objects.get(nombre=anun2.nombre)
    img3 = Proveedor.objects.get(nombre=anun3.nombre)
    datos = {
         'fecha1': ultimoParche.fechaParche,
         'fecha2': penultimoParche.fechaParche,
         'desc1' : ultimoParche.descParche,
         'desc2' : penultimoParche.descParche,
         'img'   : Proov.imagen,
         'img4'   : Proov1.imagen,
         'titulo1': anun1.nombre,
         'titulo2': anun2.nombre,
         'titulo3':anun3.nombre,
         'descr1' : anun1.descAnuncio,
         'descr2' : anun2.descAnuncio,
         'descr3' : anun3.descAnuncio,
         'img1' : img1.imagen,
         'img2' : img2.imagen,
         'img3' : img3.imagen
     }
    return render(request,'combate\index.html',datos)

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