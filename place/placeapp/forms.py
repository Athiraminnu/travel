from django import forms
from . models import place2visit

class form1(forms.ModelForm):
    class Meta:
        model = place2visit
        fields = ['name', 'about', 'img']