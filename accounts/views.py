from email import message
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)
    
    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso.')
        return redirect('dashboard')
    
def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha')

    if not nome or not sobrenome or not email or not usuario \
            or not senha or not senha2:
        messages.error(request, "Nenhum campo pode estar vazio.")
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, "Email inválido.")
        return render(request, 'accounts/register.html')

    if len(senha) < 6:
        messages.error(request, "A senha precisa ter no mínimo 6 caracteres.")
        return render(request, 'accounts/register.html')
    
    if len(usuario) < 6:
        messages.error(request, "O usuário precisa ter no mínimo 6 caracteres.")
        return render(request, 'accounts/register.html')

    if senha != senha2:
        messages.error(request, "As senhas não são iguais.")
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, "O nome de usuário já existe.")
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, "O email já foi cadastrado.")
        return render(request, 'accounts/register.html')

    messages.success(request, "Registrado com sucesso.")

    user = User.objects.create_user(username=usuario, email=email, 
                                    password=senha, first_name=nome, 
                                    last_name=sobrenome)
    return redirect('login')

@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', { 'form': form })

    #request.FILES se refere à imagem
    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, "Erro ao submeter formulário.")
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', { 'form': form })

    form.save()
    messages.success(request, f'Contato {request.POST.get("nome")} salvo com sucesso!')
    return redirect('dashboard')

    
