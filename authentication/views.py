from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def Registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {
        'form':form
    }
    return render(request, 'registration.html', context)


def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        form = AuthenticationForm()

    context = {
        'form':form
    }
    return render(request, 'login.html', context)

def LogoutView(request):
    logout(request)
    return redirect('login')