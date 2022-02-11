from django import forms
from models import Editor

class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }



    """
    nombre = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    domicilio = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ciudad = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pais = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    """