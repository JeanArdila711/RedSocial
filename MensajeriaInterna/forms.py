from django import forms
from .models import Message
from users.models import User

class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Mensaje para',
        widget=forms.Select(attrs={'class': 'form-select bg-dark-subtle'})  # Agregar clase Bootstrap aquí
    )

    class Meta:
        model = Message
        fields = ['receiver', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control bg-dark-subtle'}),  # Agregar clase Bootstrap aquí
        }
        labels = {
            'content': 'Contenido',
        }

class MessageForm2(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control bg-dark-subtle'}),  # Agregar clase Bootstrap aquí
        }
        labels = {
            'content': 'Mensaje',
        }

