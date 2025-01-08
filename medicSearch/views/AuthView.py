from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from medicSearch.forms.AuthForm import LoginForm, RegisterForm

from django.contrib.auth.models import User


def login_view(request):
    loginForm = LoginForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                _next = request.POST.get('next')
                if _next is not None:
                    return redirect(_next)
                else:
                    return redirect('/')
            else:
                message = {
                    'type': 'danger',
                    'text': 'Usuário ou senha inválidos.'
                }

    context = {
        'form': loginForm,
        'message': message,
        'title': 'Login',
        'button_text': 'Entrar',
        'link_text': 'Registar',
        'link_href': '/register'
    }

    return render(request, template_name='auth/auth.html', context=context)


def register_view(request):
    registerForm = RegisterForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():
            verifyUsername = User.objects.filter(username=username).first()
            verifyEmail = User.objects.filter(email=email).first()

            if verifyUsername is not None:
                message = {
                    'type': 'danger',
                    'text': 'Usuário já cadastrado.'
                }
            elif verifyEmail is not None:
                message = {
                    'type': 'danger',
                    'text': 'Email já cadastrado.'
                }
            else:
                user = User.objects.create_user(username, email, password)

                if user is not None:
                    message = {
                        'type': 'success',
                        'text': 'Cadastro realizado com sucesso.'
                    }
                else:
                    message = {
                        'type': 'danger',
                        'text': 'Erro ao cadastrar.'
                    }

        context = {
            'form': registerForm,
            'message': message,
            'title': 'Registrar',
            'button_text': 'Registrar',
            'link_text': 'Login',
            'link_href': '/login'
        }

        return render(request, template_name='auth/auth.html', context=context)

    context = {
        'form': registerForm,
        'message': message,
        'title': 'Registrar',
        'button_text': 'Registrar',
        'link_text': 'Login',
        'link_href': '/login'
    }

    return render(request, template_name='auth/auth.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/login')