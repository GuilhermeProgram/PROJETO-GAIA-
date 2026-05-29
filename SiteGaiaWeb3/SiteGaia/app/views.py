from django.contrib.admindocs.utils import non_capturing_group_matcher
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contato
from projeto import settings


def home(request):
    return render(request, 'index.html')

def equipe(request):
    return render(request, 'equipe.html')

def projetos(request):
    return render(request, 'Apresentação.html')

def contato(request):

    if request.method == 'POST':
        print("FORMULÁRIO RECEBIDO")
        nome=request.POST.get('nome')
        email=request.POST.get('email')
        assunto=request.POST.get('assunto')
        mensagem=request.POST.get('mensagem')

        Contato.objects.create(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )

        send_mail(
            subject=f'Contato do site: {assunto}',
            message=f'''
Nome: {nome}

Email: {email}

Mensagem: 
{mensagem}
''',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['ygorbgomes@gmail.com'],
            fail_silently=False
        )

        return redirect('/')
    return render(request,'contato.html')


