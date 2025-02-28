# django-tutorial 

*to create project
-django-admin startproject project_name

*to run server 
-python manage.py runserver

*to change port or declare port
-python manage.py runserver 4001

*templates folder includes html file
*static folder include all css ,js file
*media file store dynamic file such as image

migrate means create default table 

migration 
-python manage.py migrate

*create superuser
python manage.py createsuperuser

*to render pages
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

*how many types routes make
1.int
2.str
3.slug eg.hello-ws-iip

