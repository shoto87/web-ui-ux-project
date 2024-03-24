from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#added here
from django import forms
from .models import Profile
#till here'

class SignUpForm(UserCreationForm):

    class Meta:

        model = User
        fields = ["username","email","password1","password2"]

#added here
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
#till here