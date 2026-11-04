from django.db import models

class MembrosEquipe(models.Model):
    nome=models.CharField(max_length=100)
    cargo=models.CharField(max_length=100)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='equipe/')

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    criado_em= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Projetos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField(blank=True,null=True)
    foto = models.ImageField(upload_to='Apresentação/',blank=True,null=True)

    def __str__(self):
        return self.nome