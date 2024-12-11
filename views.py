from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import PetForm, CareGiverForm
from .models import Pet, CareGiver


def index(request):
    pets = Pet.objects.all()
    caregivers = CareGiver.objects.all()  # Query all CareGiver objects
    return render(request, 'index.html', {'pets': pets, 'caregivers': caregivers})


@login_required(login_url='login')
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def topics_detail(request):
     return render(request, 'topics-detail.html')

def giver_details(request):
     return render(request, 'giver_details.html')

def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect('/')
    else:
        form = PetForm()
    return render(request, 'add_pet.html', {'form': form})


def add_caregiver(request):

    if request.method == "POST":
        form = CareGiverForm(request.POST, request.FILES)
        if form.is_valid():
            caregiver = form.save(commit=False)
            caregiver.user = request.user
            caregiver.save()
            return redirect('/')
    else:
        form = CareGiverForm()
    return render(request, 'add_caregiver.html', {'form': form})

