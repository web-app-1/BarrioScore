from django import forms
from .models import Resena
from .models import Residencial
from .models import Promotor


class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['residencial', 'calificacion', 'comentario', 'hashtags']
        labels = {
            'residencial': 'Residencial',
            'calificacion': 'Calificación',
            'comentario': 'Comentario',
            'hashtags': 'Hashtags (separados por comas)',
        }
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu reseña aquí'}),
            'hashtags': forms.TextInput(attrs={'placeholder': 'Agrega hashtags separados por comas'}),
        }


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