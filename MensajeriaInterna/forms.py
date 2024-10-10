from django import forms
from .models import Message
from users.models import User

class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Usuario",
        widget=forms.Select(attrs={'class': 'form-select'})  # Agregar clase Bootstrap aquí
    )

    class Meta:
        model = Message
        fields = ['receiver', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),  # Agregar clase Bootstrap aquí
        }
        labels = {
            'content': 'Mensaje',
        }