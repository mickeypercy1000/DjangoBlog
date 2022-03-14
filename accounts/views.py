from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home/')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Invalid Username or Password. Please try again"))
            return redirect('login')
    else:
        return render(request, 'Users/Login.html')

def RegisterView(request):
    return render(request, "Users/Register.html")