# estacio-gestao-ferramentas

#criar venv
<!-- https://www.youtube.com/watch?v=LndJOSwRYOM&list=PLHWfNMxB2F4HdKbo8zdgXyxVDOxH429Ko&index=5 -->
python3 -m venv venv

#ativar
source venv/bin/activate

#desativar
deactivate

#instalar pacote
python -m pip install <package-name>

#django
#https://docs.djangoproject.com/en/4.1/
pip install Django==4.1.6

#projeto django
django-admin startproject ferramentas


#criar app
cd ferramentas
python manage.py startapp contas

python manage.py migrate

python manage.py runserver

#definir porta
python manage.py runserver 7000

control + c

python manage.py createsuperuser

cleydson
123456

python manage.py runserver 7000
http://127.0.0.1:7000/admin













