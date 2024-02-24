import pytest
from .forms import UsuarioForm
from django.urls import reverse


@pytest.mark.django_db
def test_validar_documento(client):
    url = reverse('validar_documento')
    response = client.post(url, {'documento': '1234567890'})
    assert response.status_code == 302


@pytest.mark.django_db
def test_guardar_datos(client):
    url = reverse('guardar_datos')
    response = client.post(url, {'dni': '1234567890', 'nombre': 'Nombre',
                                 'apellido': 'Apellido',
                                 'email': 'correo@ejemplo.com',
                                 'monto_solicitado': 100})
    assert response.status_code == 200


def test_usuario_form_valid():
    form_data = {'dni': '1234567890', 'nombre': 'Nombre',
                 'genero': 'Femenino',
                 'apellido': 'Apellido',
                 'email': 'correo@ejemplo.com',
                 'monto_solicitado': 100}
    form = UsuarioForm(data=form_data)
    assert form.is_valid()
