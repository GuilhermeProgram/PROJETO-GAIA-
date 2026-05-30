from django.contrib.admindocs.utils import non_capturing_group_matcher
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contato
from projeto import settings
from .models import MembrosEquipe
from .models import Projetos

def home(request):
    return render(request, 'index.html')

def equipe(request):

    integrantes = MembrosEquipe.objects.all()

    return render(request,
                  'equipe.html',
                  {'integrantes' : integrantes})

def projetos(request):

    lista_projetos = Projetos.objects.all()

    return render(request, 'Apresentação.html', {
        'projetos': lista_projetos
    })

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


