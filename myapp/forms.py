from django import forms
from django.forms import ModelForm
from .models import People
class RecordForm(forms.Form):
    name = forms.CharField(max_length=100)
    birthday = forms.DateField()
    country = forms.CharField(max_length=100)
    organization = forms.CharField(max_length=100)
    role = forms.CharField(max_length=100)

class RecordUpdateForm(ModelForm):
    class Meta:
        model = People
        fields = ['name','birthday','country','organization','role']
