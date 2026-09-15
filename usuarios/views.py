from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib import messages

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    username = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'Já existe um usuário com este username.')
        return render(request, 'cadastro.html')

    user = User.objects.create_user(username=username, email=email, password=senha)
    user.save()
    messages.success(request, 'Usuário cadastrado com sucesso! Faça login.')
    return redirect('login')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    # Agora pegamos o email do formulário
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    try:
        # Procuramos no banco qual usuário tem esse e-mail
        user_obj = User.objects.get(email=email)
        username_encontrado = user_obj.username
    except User.DoesNotExist:
        username_encontrado = None

    # O Django autentica usando o username vinculado àquele e-mail
    user = authenticate(username=username_encontrado, password=senha)
    
    if user is not None:
        login_django(request, user)
        return redirect('dashboard')
    else:
        messages.error(request, 'E-mail ou senha inválidos.')
        return render(request, 'login.html')

def logout_view(request):
    logout_django(request)
    return redirect('login')