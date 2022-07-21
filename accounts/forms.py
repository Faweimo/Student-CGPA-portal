from django import forms

from accounts.utils import matric_no

# Login Form
class LoginForm(forms.Form):
    email = forms.CharField(required=True,widget=forms.TextInput(attrs={'type':'email','class':'form-control','placeholder':'email'}))        
    # matric_no = forms.CharField(required=True,widget=forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'matric_no'}))        
    password = forms.CharField(widget=forms.TextInput(attrs={'type':'password','class':'form-control','placeholder':'Password'})) 