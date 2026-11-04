# Projeto Gaia

Site institucional da **Gaia Soluções Sustentáveis**, iniciativa de Itaipuaçu (Maricá, RJ) que trabalha com compostagem, gestão de resíduos orgânicos e educação ambiental. O projeto foi desenvolvido em **Django** e tem páginas de história, projetos, equipe e contato, com conteúdo gerenciado por um painel administrativo.

> Projeto em equipe, desenvolvido para uma ONG. Status: em desenvolvimento.

## Funcionalidades

- **Nossa História:** apresentação da organização, origem e linha do tempo (2019 em diante).
- **Projetos:** lista de projetos com descrição, data e foto, carregada do banco de dados.
- **Equipe:** cards dos integrantes (nome, cargo, descrição e foto), também vindos do banco.
- **Contato:** formulário que salva a mensagem no banco e envia um e-mail de aviso por SMTP.
- **Painel administrativo (`/admin`):** cadastro de projetos e integrantes, e consulta das mensagens recebidas, com busca e filtro por data.

## Tecnologias

| Camada | Uso |
| --- | --- |
| Back-end | Python, Django 6 |
| Banco de dados | SQLite |
| Front-end | HTML, CSS (templates Django) |
| Imagens | Pillow (`ImageField`) |
| E-mail | SMTP (Gmail) |

## Estrutura

```
gaia-site/
├── manage.py
├── config/           # configurações do Django (settings, urls, wsgi)
└── app/
    ├── models.py     # MembrosEquipe, Projetos, Contato
    ├── views.py      # home, equipe, projetos, contato
    ├── urls.py       # rotas do site
    ├── admin.py      # configuração do painel administrativo
    ├── templates/    # index, projetos, equipe, contato
    └── static/       # CSS e imagens
```

A pasta `prototipo-estatico/` guarda o protótipo inicial do site, em HTML puro, sem Django.

## Modelo de dados

- `MembrosEquipe`: nome, cargo, descrição, foto.
- `Projetos`: nome, descrição, data (opcional), foto (opcional).
- `Contato`: nome, e-mail, assunto, mensagem, data de criação.

## Como rodar

Pré-requisitos: Python 3.12 ou superior.

```bash
git clone https://github.com/GuilhermeProgram/PROJETO-GAIA-.git
cd PROJETO-GAIA-/gaia-site

python -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate

pip install django pillow python-dotenv

cp .env.example .env             # preencha os valores (veja abaixo)
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/` para o site e `http://127.0.0.1:8000/admin/` para o painel. O banco começa vazio: cadastre projetos e integrantes pelo painel para vê-los nas páginas.

### Variáveis de ambiente

| Variável | Descrição |
| --- | --- |
| `DJANGO_SECRET_KEY` | chave secreta do Django |
| `DJANGO_DEBUG` | `True` em desenvolvimento |
| `EMAIL_HOST_USER` | conta que envia o aviso de contato |
| `EMAIL_HOST_PASSWORD` | senha de app dessa conta |
| `CONTACT_RECIPIENT` | e-mail que recebe as mensagens do formulário |

## Equipe

- **Guilherme:** front-end. Páginas em HTML e estilos em CSS (Nossa História, Projetos, Equipe e Contato).
- **Ygor:** back-end em Django (modelos, views, rotas, painel administrativo e envio de e-mail).
- **Isis:** documentação do projeto.

## Próximos passos

- Adicionar testes automatizados para as views e o formulário de contato.
- Validar o formulário com `forms.py` do Django em vez de ler o `POST` direto.
- Configurar o projeto para deploy (`ALLOWED_HOSTS`, arquivos estáticos e mídia).
- Revisar a acessibilidade e o layout para celular.
