from django import forms
from . models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full'}),  # Use `forms.TextInput` instead of `forms.CharField`.
            'description': forms.Textarea(attrs={'class': 'w-full'}),
        }