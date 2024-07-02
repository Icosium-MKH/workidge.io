from django import forms 
from .models import Developer,Recruiter

class DeveloperRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Developer
        fields = ['name', 'surname', 'email','pn','title','password']

class RecruiterRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Recruiter
        fields = ['name', 'surname', 'email','pn','title','company','password']


