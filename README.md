# Projeto Seabrix Django

Este projeto é uma cópia funcional da Netflix desenvolvida para fins acadêmicos. Ele foi criado utilizando Django e integra várias tecnologias modernas, destacando-se pela implementação de Class-Based Views, estilização avançada e autenticação de usuários.

## 🌐 Caso queira testar esse projeto funcionando de forma online

[Clique aqui para acessar](https://djangoseabrix-production.up.railway.app/ "target=_blank")

## 📝 Descrição

O objetivo principal foi replicar aspectos fundamentais de plataformas de streaming como a Netflix. O projeto inclui:

* Gerenciamento de usuários: Cadastro e autenticação.
* Estilização CSS: Uso combinado de Bootstrap e Tailwind CSS.
* Gerenciamento de conteúdo: CRUD de filmes com imagens e descrições. (É possível criar novos filmes e séries a partir do admin do Django)
* Banco de dados: Integração com PostgreSQL.

## 🛠️ Recursos Principais

* **Class-Based Views:** Simplificação da lógica de controle e melhor organização.
* **Autenticação de Usuário:** Sistema de login e logout com segurança.
* **Banco de Dados Relacional:** Estruturação eficiente para manipulação de dados de filmes.
* **Estilização Responsiva:** Interfaces otimizadas para diferentes dispositivos.

## 📂 Estrutura do Projeto
```
Diogo-seabra-DjangoSeabrix/
    ├── manage.py
    ├── seabrix/ # Configurações principais do projeto Django.
    │   ├── settings.py
    │   ├── __init__.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── requirements.txt  # Dependências do projeto.
    ├── runtime.txt
    ├── filme/    # App principal do projeto.
    │   ├── models.py
    │   ├── __init__.py
    │   ├── novos_context.py
    │   ├── urls.py
    │   ├── tests.py
    │   ├── apps.py
    │   ├── migrations/
    │   │   ├── __init__.py
    │   │   └── 0001_initial.py
    │   ├── forms.py
    │   ├── templatetags/
    │   │   ├── __init__.py
    │   │   └── filtros.py
    │   ├── admin.py
    │   ├── views.py
    │   └── templates/
    │       ├── homefilmes.html
    │       ├── logout.html
    │       ├── detalhesfilme.html
    │       ├── login.html
    │       ├── detalhesserie.html
    │       ├── criarconta.html
    │       ├── homepage.html
    │       ├── editarperfil.html
    │       └── pesquisa.html
    ├── LICENSE
    ├── README.md
    ├── templates/  # Templates HTML reutilizáveis.
    │   ├── base.html
    │   └── navbar.html
    ├── Procfile   # Configurações para deploy no Railway.
    └── static/  # Arquivos CSS, JavaScript e imagens.
        ├── thumb_filmes/
        ├── images/
        └── css/
            └── styles.css
```

## Pré-requisitos

* Python 3.8+
* Django 4.x
* PostgreSQL
* Ambiente virtual configurado.


## 🚀 Caso queira testar esse projeto de forma local, siga o passo a passo de instalação e execução:

1. Clone o repositório:
   ```bash
   git clone https://github.com/Diogo-seabra/DjangoSeabrix.git

2. Navegue até a pasta:
   ```bash
   cd DjangoSeabrix
   
3. Crie um ambiente virtual:
   ````bash
   python -m venv venv
   
4. Ative o ambiente virtual:
   ````bash
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   
4. Instale as dependências:
   ````bash
   pip install -r requirements.txt

5. Execute as migrações:
   ````bash
   python manage.py migrate

6. Crie um superusuário:
   ````bash
   python manage.py createsuperuser

7. Inicie o servidor:
   ````bash
   python manage.py runserver
   
8. Acesse o painel administrativo: <br>
   Abra seu navegador e acesse http://127.0.0.1:8000/admin/ para fazer login com as credenciais do seu superusuário. E então, adicione os filmes e séries de sua preferência que serão exibidos no site
   
   ![image](https://github.com/user-attachments/assets/c5f55573-564c-4b41-b2aa-5374483aa826)


## 🫂 Contribuições

Contribuições são bem-vindas! Por favor, envie suas sugestões ou pull requests.

## 👤 Autor

Desenvolvido por Diogo Seabra.

Sinta-se à vontade para usar este projeto como referência ou ponto de partida para outros trabalhos!



   
