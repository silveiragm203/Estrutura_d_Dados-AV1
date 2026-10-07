# COMANDOS DO DJANGO

1. ``pip install django ``-> Instala o Django no projeto.
2. ``django-admin startproject nome_do_projeto .`` -> Criando um novo projeto em django.
3. ``python manage.py runserver`` -> Subindo o servidor.
4. ``python manage.py startapp nome_do_app`` -> Criando um novo app.
5. ``python manage.py migrate`` ->  Realiza as migrações(ativa) do projeto.
6. ``python manage.py createsuperuser`` -> Criar um novo super usuário.
7. ``python manage.py changepassword nomedousuario`` -> Altera a senha, caso você esqueça.
8. ``python manage.py makemigrations`` -> Cria/gera um novo pacote de migração (Útil para novo app e alteração do BD).


# ATIVIDADE
1. Criar um model para o médico com as informações: 
 - Nome
 - Sobrenome
 - E-mail
 - Data da Criação
 - Telefone
 - CRM (6 digitos), será string
 - Especialidade 
 - Mensagem
 - Ativo = True 

 2. Na Exibição do Portal administrativo, deverá ser apresentado:
 - Id, Nome, email, telefone, especialidade, crm, ativo 
