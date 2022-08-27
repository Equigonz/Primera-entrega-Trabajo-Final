from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                context = {'message':f'Bienvenido {username}!!'}
                return render(request, 'index.html', context = context)
        
        form  = AuthenticationForm()
        return render(request, 'login.html', {'error':'Usuario Incorrecto', 'form': form})
    
    elif request.method == 'GET': 
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {'errors':form.errors}
            form = UserCreationForm()
            context['form'] = form
            return render(request, 'register.html', context)

    elif request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
