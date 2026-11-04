from django.contrib import admin
from .models import MembrosEquipe
from .models import Contato
from .models import Projetos

@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'data'
    )

@admin.register(MembrosEquipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display =(
        'id',
        'nome',
        'cargo'
    )

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display =(
        'nome',
        'email',
        'assunto',
        'criado_em'
    )

    readonly_fields =(
        'nome',
        'email',
        'assunto',
        'mensagem',
        'criado_em'
    )

    search_fields =(
        'nome',
        'email',
        'assunto'
    )

    list_filter =(
        'criado_em',
    )

    ordering =(
        '-criado_em',
    )