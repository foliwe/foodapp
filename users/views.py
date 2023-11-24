from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import RegisterForm
from django.contrib.auth import authenticate


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, f'Account created sucessfully')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, f'Username or Password is incorrect')
#             return redirect('login')
#     else:

#         return render(request, 'users/login.html')

@login_required()
def profile(request):
    return render(request, 'users/profile.html')
