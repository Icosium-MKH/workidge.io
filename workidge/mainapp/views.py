from django.shortcuts import render, redirect
from .forms import DeveloperRegistrationForm, RecruiterRegistrationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import JobOffer
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,"home.html")


def register(request):
    developer_form = DeveloperRegistrationForm()
    recruiter_form = RecruiterRegistrationForm()
    return render(request, 'register.html', {'developer_form': developer_form, 'recruiter_form': recruiter_form})


def developer_registration(request):
    if request.method == 'POST':
        form = DeveloperRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Optionally log in the user after registration
            #login(request, user)
            #return home(request)
            return redirect('home')
    else:
        form = DeveloperRegistrationForm()
        return register(request)

def recruiter_registration(request):
    if request.method == 'POST':
        form = RecruiterRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Optionally log in the user after registration
            #login(request, user)
            #return home(request)
            return redirect('home')
    else:
        form = RecruiterRegistrationForm()
        return register(request)


@login_required
def offers(request):
    job_offers = JobOffer.objects.all()
    return render(request, 'offers.html', {'job_offers': job_offers})  # Adjust this as per your application logic


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Redirect to the home page after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('home') 