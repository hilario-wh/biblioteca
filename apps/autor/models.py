from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return '{} {}'.format(self.nombre, self.apellidos)