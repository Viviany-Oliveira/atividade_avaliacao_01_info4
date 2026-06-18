from django.shortcuts import render, redirect

def home(request):
    return render(request, 'core/home.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        ocupacao = request.POST.getlist('ocupacao')
        
        context = {
            'nome': nome,
            'cpf': cpf,
            'data_nascimento': data_nascimento,
            'ocupacao': ', '.join(ocupacao)
        }
        return render(request, 'core/sucesso.html', context)
    
    return render(request, 'core/cadastro.html')

def sucesso(request):
    # Esta view é chamada diretamente quando acessa /sucesso/
    return render(request, 'core/sucesso.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if email == 'admin@email.com' and senha == '123':
            return redirect('perfil')
        else:
            return redirect('login')
    
    return render(request, 'core/login.html')

def perfil(request):
    return render(request, 'core/perfil.html')