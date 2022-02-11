from django import forms
from models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            'titulo',
            'autores',
            'editor',
            'fecha_publicacion',
            'portada',
        ]

        labels = {
            'titulo': 'Titulo',
            'autores': 'Autores',
            'editor': 'Editor',
            'fecha_publicacion': 'Fecha Publicacion',
            'portada': 'portada',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autores': forms.CheckboxSelectMultiple(),
            'editor': forms.Select(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'portada': forms.ClearableFileInput(),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if titulo.lower() == 'abc':
            raise forms.ValidationError("No es un titulo valido")
        return titulo