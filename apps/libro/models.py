from django.db import models
from apps.autor.models import Autor
from apps.editor.models import Editor

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to='portadas')