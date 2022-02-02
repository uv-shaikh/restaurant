from django import forms
from .models import Signup,Product

class signupforms(forms.ModelForm):
    class Meta:
        model = Signup
        fields=['username','email','phone','password','confirmpassword']

class editform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']

class editprofile(forms.ModelForm):
    class Meta:
        model = Signup
        fields=['username','email','phone']
