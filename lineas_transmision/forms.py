from django import forms
from .models import InspeccionLinea

class InspeccionLineaForm(forms.ModelForm):
    class Meta:
        model = InspeccionLinea
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

