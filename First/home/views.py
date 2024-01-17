from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    # vars = {
    #     'variable1': 'This is sent',
    #     'variable2': 'This is sent 2',
    #     'variable3': 'This is sent 3'
    # }

    if request.user.is_anonymous:
        return render(request, 'login.html')

    return render(request, 'index.html')
    # return HttpResponse("This is home page")

def registerUser(request):

    if request.method == "POST":
        f_name = request.POST.get('name')
        l_name = request.POST.get('surname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html')

        # Create the user

        user = User.objects.create_user(username, email, password)
        user.first_name = f_name
        user.last_name = l_name
        user.save()
        messages.success(request, 'Your account has been created successfully!')

    return render(request, 'register.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user has entered correct credentials

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'index.html')

        else:
            messages.error(request, 'Invalid credentials, please try again!')
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request, 'contact.html')

def services(request):
    return HttpResponse("This is services page")    
