from django.shortcuts import render, redirect
from .forms import DeveloperRegistrationForm, RecruiterRegistrationForm, MyProfileForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import JobOffer,Competence,Developer
from .serializers import CompetenceSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view



# Create your views here.
def home(request):
    return render(request, "home.html")


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
            # login(request, user)
            # return redirect('home')  # Redirect to home after registration
            return redirect('home')
        else:
            # If form is invalid, re-render the registration form with errors
            return render(request, 'register.html', {'developer_form': form, 'recruiter_form': RecruiterRegistrationForm()})
    else:
        form = DeveloperRegistrationForm()
        return render(request, 'register.html', {'developer_form': form, 'recruiter_form': RecruiterRegistrationForm()})


def recruiter_registration(request):
    if request.method == 'POST':
        form = RecruiterRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Optionally log in the user after registration
            # login(request, user)
            # return redirect('home')  # Redirect to home after registration
            return redirect('home')
        else:
            # If form is invalid, re-render the registration form with errors
            return render(request, 'register.html', {'developer_form': DeveloperRegistrationForm(), 'recruiter_form': form})
    else:
        form = RecruiterRegistrationForm()
        return render(request, 'register.html', {'developer_form': DeveloperRegistrationForm(), 'recruiter_form': form})


@login_required
def offers(request):
    job_offers = JobOffer.objects.all()
    return render(request, 'offers.html', {'job_offers': job_offers})  # Adjust this as per your application logic


def login(request):
    next_url = request.POST.get('next', request.GET.get('next', '/'))
    print(f"Next URL: {next_url}")
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if next_url and next_url != '/':
                    return redirect(next_url)
                else:
                    return redirect('home')
    else:
        form = AuthenticationForm()        
    
    return render(request, 'login.html', {'form': form})

#Think about it ...
def logout(request):
    auth_logout(request)
    return redirect('home')


@login_required
def profile(request):
    # Assuming you have a way to identify the current logged-in user (developer)
    developer = request.user.developer  # Assuming 'developer' is related to User model
    
    if request.method == 'POST':
        form = MyProfileForm(request.POST, instance=developer)
        if form.is_valid():
            form.save()
            return redirect('myprofile')  # Redirect to the profile page after saving
    else:
        form = MyProfileForm(instance=developer)
    
    context = {
        'form': form,
    }
    return render(request, 'profile.html', context)



@api_view(['GET'])
def get_competence_by_dev(request, developer_id):
    try:
        developer = Developer.objects.get(id=developer_id)
    except Developer.DoesNotExist:
        return Response({'error': 'Developer not found'}, status=404)
    
    competences = developer.skills.all()  # Assuming 'skills' is the related name in Developer model
    serializer = CompetenceSerializer(competences, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_competence(request):
    competences = Competence.objects.all()
    serializer = CompetenceSerializer(competences, many=True)
    return Response(serializer.data)