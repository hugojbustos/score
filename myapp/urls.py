from django.contrib.auth import views as auth_views
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('validar-documento/', views.validar_documento, name='validar_documento'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('cargar-datos/<str:dni_validado>/', views.cargar_datos, name='cargar_datos'),
    path('guardar-datos/', views.guardar_datos, name='guardar_datos'),
    path('editar/<int:pk>/', views.editar, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar, name='eliminar'),
]