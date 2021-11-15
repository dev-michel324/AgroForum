from django.http.response import HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseRedirect
from .forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django import http
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserChangeForm, PasswordChangeForm
from .models import User

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    msg = 'Login succesfully.', username
                    messages.info(request, 'Login efetuado com sucesso, '+username+'.')
                    # return redirect('post:posts')
                    return HttpResponseRedirect('/main')
                else:
                    messages.error(request, 'Username or password invalid.')
            else:
                messages.error(request, 'Username or password invalid.')
        form = AuthenticationForm()
        return render(request, 'user/index.html', {'form': form})
    return HttpResponseRedirect('/main')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successfull.')
            return HttpResponseRedirect('/')
            # return redirect('user:index')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})

def loggout(request):
    logout(request)
    messages.info(request, 'Successful logout.')
    return HttpResponseRedirect('/')

# @login_required
def editUser(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.id)
        form = UserChangeForm(instance=user)

        if request.method=='POST':
            form = UserChangeForm(request.POST, instance=user)

            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                messages.info(request, 'Profile updated with successfull.')
                return HttpResponseRedirect('/main/profile')
            else:
                return render(request, 'user/edit_data.html', {'form': form, 'userform': user})
        elif(request.method == 'GET'):
            return render(request, 'user/edit_data.html', {'form': form, 'userform' : user})
    return HttpResponseForbidden()

def password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.info(request, 'Password updated with success.')
                return HttpResponseRedirect('/main/profile')
            else:
                messages.error(request, 'Invalid data.')
                # return render(request, 'user/edit_pass.html', {'form': form})
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'user/edit_pass.html', {'form': form})
    return HttpResponseForbidden()