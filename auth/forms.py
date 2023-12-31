from django.contrib.auth.forms import UserCreationForm # форма для регистрации
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreationCustomForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
  
        self.fields['username'].widget.attrs['class'] = 'form-control-lg'
        self.fields['password1'].widget.attrs['class'] = 'form-control-lg'
        self.fields['password2'].widget.attrs['class'] = 'form-control-lg'
        self.fields['first_name'].widget.attrs['class'] = 'form-control-lg'
        self.fields['last_name'].widget.attrs['class'] = 'form-control-lg'


    class Meta:
        model = User 
        fields = ("username", 'password1','password2','first_name', 'last_name')