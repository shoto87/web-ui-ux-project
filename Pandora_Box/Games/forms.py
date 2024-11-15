from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#added here
from django import forms
from .models import Profile ,Downloads
#till here'

class SignUpForm(UserCreationForm):

    class Meta:

        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

class DownloadForm(forms.ModelForm):
    class Meta:
        model = Downloads
        fields = ['user', 'product']
#added here
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
#till here