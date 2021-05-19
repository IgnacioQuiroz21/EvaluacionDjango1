from django.shortcuts import render


def Actualizacion(request):
    actua={"nombre":"Actualizacion 15/04","descripcion":"Conoce detalles de la actualizacion."}

    return render(request, 'index.html', actua)

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



