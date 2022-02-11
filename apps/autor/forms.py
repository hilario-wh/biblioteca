from django import forms
from models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }