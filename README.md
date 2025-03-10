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

*dynamic url
-path("aboutus/<type:parameter>",views.courseid)

add template path : setting.py->template->dir->BASE_DIR,'templates'

*to add djngo file data on html file
-data={
          'title':"home Page",
          'bdata':'welcome to wscubetech',
          'clist':['PHP','JAVA','DJANGO'],
          'student':[{'name':"swapnil",'phone':9856856525}, 
          {'name':'testing','phone':8556526465}]
     }
-return render(request,'index.html',data)
on html:<title>{{title}}<title>

*using django template for loop
-{%for n in clist%}
      <div>{{forloop.counter0}} {{n}}<div>
          <div>{{forloop.first}} {{n}}<div>
               <div>{{forloop.last}} {{n}}<div>
          {% endfor %}
          <table border='1' cellpadding='10'>
               <tr>
                    <th>sr. no</th>
                    <th>Name</th>
                    <th>Phone number</th>
               </tr>
     {%for i in student%}
     <tr>
          <th>{{forloop.counter}}</th>
          <th>{{i.name}}</th>
          <th>{{i.phone}}</th>
     </tr>
     {% endfor %}
          </table>

*if else statement in django template
data={'number':[10,20,30,40,50]}
{%for n in number%}
          {% if n > 20 %}
        <div>{{n}}</div> 
        {% else %}
        {{'name'|length}} 
          {%endif%}
          {%endfor%}

to add static folder
STATICFILES_DIRS=[BASE_DIR,'static']

to add header or footer
-{% include "header.html" %}

extend & include Django template
*base.html
{% include 'header.html' %}
{% block content %}
{% endblock %}
*index.html
{% extends "base.html" %}
{% block content %}
html code 
{% endblock %}

*url template tag
href="/about-us"
or
path('',views.home,name="home")
href={% url 'home' %}

url highlighting
style.css
.active{
background-color:blue 
}

class="{% if request.path =='/about-us'%} actve {% endif %}"
}


get data from form to django file (views.js)
 n1=int(request.GET['num1'])
          n2=int(request.GET['num2'])
          n1=request.GET.get('num1')
          n2=request.GET.get('num2')

get-get data using url

post -to get data using http request
 n1=int(request.GET['num1'])
          n2=int(request.GET['num2'])
          n1=request.POST.get('num1')
          n2=request.POST.get('num2')

*create module in python 
-python manage.py startapp service
-python manage.py makemigration 
-python manage.py migrate

create model in models.py
import model in admin.py
admin.py
-from django.contrib import admin
from service.models import service
class serviceadmin(admin.ModelAdmin):
     list_display=['service_icon','service_title','service_description']

admin.site.register(service,serviceadmin)

# Register your models here.

models.py
from django.db import models
class service(models.Model):
     service_icon = models.CharField(max_length=50)
     service_title = models.CharField(max_length=50)
     service_description = models.TextField()
# Create your models here.

get data on html page
-serviceData=service.objects.all().order_by('-service_description')[1:3]-slicing data(limit)
-data={'serviceData':serviceData}                                  |  |
dash before column name is decending                            start end

to filter data
newsdetail=news.objects.filter(news_title=st)

# to change admin password
python manage.py changepassword username

#pagination
serviceData=service.objects.all()
          Paginator=Paginator(serviceData,2)
          page_number=request.GET.get('page')
          servicefinalData=Paginator.get_page(page_number)
          total_pages=servicefinalData.paginator.num_pages

          data={'serviceData':servicefinalData,
                'totalpagelist':[n+1 for n in range(total_pages)]}
          return render(request,'services.html',data)
{% if serviceData.has_previous and serviceData.has_next % }
print("hi")
{% endif %}

#form data to database
 n=''
     if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          username=request.POST.get('Username')
          password=request.POST.get('password')
          en=query(name=name,email=email,username=username,password=password)
          en.save()
          n='data saved successfully'
          
