# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('portada', models.ImageField(upload_to=b'portadas')),
                ('autores', models.ManyToManyField(to='autor.Autor')),
                ('editor', models.ForeignKey(to='editor.Editor')),
            ],
        ),
    ]
