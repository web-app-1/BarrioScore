from django import forms
from .models import Resena
from .models import Residencial
from .models import Promotor


class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['residencial', 'calificacion', 'comentario', 'hashtags']
    
    def __init__(self, *args, **kwargs):
        super(ResenaForm, self).__init__(*args, **kwargs)
        self.fields['residencial'].empty_label = "-----"  # Asegura que haya una opción vacía para residencial
        self.fields['calificacion'].empty_label = "-----"  # Lo mismo para calificación


class ResidencialForm(forms.ModelForm):
    class Meta:
        model = Residencial
        fields = ['nombre', 'promotor']

    def __init__(self, *args, **kwargs):
        super(ResidencialForm, self).__init__(*args, **kwargs)
        # Añadir una opción en blanco al campo promotor
        self.fields['promotor'].empty_label = "-----"

        
class PromotorForm(forms.ModelForm):
    class Meta:
        model = Promotor
        fields = ['nombre']
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Promotor.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Ya existe un promotor con este nombre.")
        return nombre