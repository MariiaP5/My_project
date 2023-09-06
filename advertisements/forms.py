from django import forms

from .models import Advertisement

from django.core.exceptions import ValidationError 

class AdvertisementForm(forms.Form):
    title       = forms.CharField(max_length=100, widget=forms.TextInput(
        {"class": "form-control-lg"}
    )) 
    description = forms.CharField(widget=forms.Textarea(
        {"class": "form-control-lg"}
    ))
    price       = forms.DecimalField(widget=forms.NumberInput(
        {"class": "form-control-lg"}
    ))
    auction     = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        {"class": "form-check-input"}
    )) # поле необязательное
    image       = forms.ImageField(widget=forms.FileInput(
        {"class": "form-control-lg"}
    ))





