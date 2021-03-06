from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/already-logged-in.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {'error': 'Invalid username or password.'}
            return render(request, 'accounts/login.html', context=context)
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html', context={})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
    return render(request, 'accounts/logout.html', context={})


def register_view(request):
    form = UserCreationForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login')
    return render(request, 'accounts/register.html', context=context)
