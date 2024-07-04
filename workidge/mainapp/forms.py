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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'] = forms.CharField(initial=self.instance.id, widget=forms.HiddenInput)
    class Meta:
        model = Developer
        fields = ['id','name','surname','email','pn','title','skills']