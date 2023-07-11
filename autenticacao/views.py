from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import password_is_valid
from django.contrib.auth.models import User


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro')
        
    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=senha,
            is_active=False   # não é para que o usuário esteja ativo assim que ele for criado, será enviado por email uma confirmação
        )
        user.save()
        return redirect('/auth/logar')
    except:
        return redirect('/auth/cadastro')


def logar(request):
    return HttpResponse('Página de login')

