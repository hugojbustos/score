from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UsuarioForm
import requests
from django.contrib.auth.decorators import login_required
from .models import Usuario


def home(request):
    return render(request, 'home.html')


def validar_documento(request):
    if request.method == 'POST':
        documento = request.POST.get('documento')
        api_endpoint = \
            f'https://api.moni.com.ar/api/v4/scoring/pre-score/{documento}'
        token = 'ZGpzOTAzaWZuc2Zpb25kZnNubm5u'
        response = requests.get(api_endpoint,
                                headers={'Authorization': f'Token {token}'})
        data = response.json()
        if data.get('status') == 'approve':
            return redirect(reverse('cargar_datos',
                                    kwargs={'dni_validado': documento}))
        else:
            return HttpResponse('El documento ingresado no es válido')

    return render(request, 'ingreso_documento.html')


def cargar_datos(request, dni_validado):
    form = UsuarioForm(initial={'dni': dni_validado})
    return render(request, 'ingreso_datos.html',
                  {'form': form, 'dni_validado': dni_validado})


def guardar_datos(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('validar_documento')
        else:
            return HttpResponse("Error en el formulario. \
                                Por favor, verifique los datos ingresados.")
    else:
        return HttpResponse("Error: se esperaba una solicitud POST.")


@login_required
def solicitudes(request):
    registros = Usuario.objects.all()
    return render(request, 'solicitudes.html', {'registros': registros})


def editar(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('solicitudes')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'editar.html', {'form': form})


def eliminar(request, pk):
    registro = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        registro.delete()
        return redirect('solicitudes')
    return render(request, 'eliminar.html', {'registro': registro})
