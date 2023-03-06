from django import forms
from . models import Perfume_search

class Perfume_search_form(forms.ModelForm):
    name_of_perfume = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control me-2", 'placeholder': 'Ex: nordestina', 'style': 'border-radius: 30px'
    }))
    class Meta:
        model = Perfume_search
        fields = ['name_of_perfume',]