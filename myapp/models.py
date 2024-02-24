from django.db import models

GENERO_CHOICES = (
    ('Femenino', 'Femenino'),
    ('Masculino', 'Masculino'),
    )


class Usuario(models.Model):
    dni = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=20, choices=GENERO_CHOICES)
    email = models.EmailField()
    monto_solicitado = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre
