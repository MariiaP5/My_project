from django import forms

from .models import Advertisement

from django.core.exceptions import ValidationError 


# class AdvertisementForm(forms.Form):
#     title       = forms.CharField(max_length=100, widget=forms.TextInput(
#         {"class": "form-control-lg"}
#     )) 
#     description = forms.CharField(widget=forms.Textarea(
#         {"class": "form-control-lg"}
#     ))
#     price       = forms.DecimalField(widget=forms.NumberInput(
#         {"class": "form-control-lg"}
#     ))
#     auction     = forms.BooleanField(required=False, widget=forms.CheckboxInput(
#         {"class": "form-check-input"}
#     )) # поле необязательное
#     image       = forms.ImageField(widget=forms.FileInput(
#         {"class": "form-control-lg"}
#     ))



class AdvertisementForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = "form-control-lg"
        self.fields['description'].widget.attrs['class'] = "form-control-lg"
        self.fields['price'].widget.attrs['class'] = "form-control-lg"
        self.fields['auction'].widget.attrs['class'] = "form-check-input"
        self.fields['image'].widget.attrs['class'] = "form-control-lg"
    class Meta:
        model = Advertisement
        fields = ('title','description','price','auction', 'image')

    def clean_title(self):
        title = self.cleaned_data['title'] 
        if title.startswith('?'):
            raise ValidationError("Заголовок не может начинаться с '?'")
        return title 

        


