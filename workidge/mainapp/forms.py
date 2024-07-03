from django import forms 
from .models import Developer,Recruiter,JobOffer

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

class JobOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = '__all__'

class MyProfileForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['name','surname','email','pn','title','skills'] 