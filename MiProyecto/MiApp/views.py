from django.shortcuts import render

# Create your views here.

from MiApp.models import Familia 

def mostrar_familia(request):
    f1 = Familia(nombre = 'Eduardo', apellido = 'Choren', edad = 63, nacimiento = '1958-12-08')
    f2 = Familia(nombre = 'Claudia', apellido = 'Grande', edad = 57, nacimiento = '1965-08-08')
    f3 = Familia(nombre = 'Agustina', apellido = 'Choren', edad = 31, nacimiento = '1991-04-08')

    return render(request, 'MiApp/Templates/MiApp/familia.html', {'Familia': [f1, f2, f3]})