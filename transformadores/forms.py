from django import forms
from .models import InspeccionTransformador

class InspeccionTransformadorForm(forms.ModelForm):
    class Meta:
        model = InspeccionTransformador
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
