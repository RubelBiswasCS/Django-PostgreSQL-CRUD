from django import forms

class RecordForm(forms.Form):
    name = forms.CharField(max_length=100)
    birthday = forms.DateField()
    country = forms.CharField(max_length=100)
    organization = forms.CharField(max_length=100)
    role = forms.CharField(max_length=100)