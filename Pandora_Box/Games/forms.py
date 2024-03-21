from django import forms

class SignUpForm(forms.Form):
    your_email = forms.CharField(widget=forms.EmailInput)
    your_password = forms.CharField(widget=forms.PasswordInput)