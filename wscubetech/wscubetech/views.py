from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .form import usersform
from service.models import service
from news.models import news
from django.core.paginator import Paginator
from contactquery.models import query
from contactquery.models import msg
from django.core.mail import send_mail,EmailMultiAlternatives
def about(request):
     return HttpResponse("welcome to wscubetech")

def home(request):
     # data={
     #      'title':"home Page",
     #      'bdata':'welcome to wscubetech',
     #      'clist':['PHP','JAVA','DJANGO'],
     #      'number':[10,20,30,40,50],
     #      'student':[
     #           {'name':"swapnil",'phone':9856856525},
     #           {'name':'testing','phone':8556526465}
     #      ]
     # }
     # return render(request,"index.html",data)
     serviceData=service.objects.all().order_by('-service_description')[1:2]
     newsdata=news.objects.all()
     
     data={'serviceData':serviceData,'newsdata':newsdata}
     return render(request,'signup.html',data)


def detail(request,slug):
     newsdetail=news.objects.get(news_slug=slug)
     # newsdetail=news.objects.all()
     data={'newsdetails':newsdetail}



     return render(request,'newsdetail.html',data)


def aboutdetail(request,courseid):
     if request.method=='GET':
          output=request.GET.get('output')
     return render(request,'about.html',{'output'})
# def userform(request):
#      final=0
#      try:
#           if request.method=='POST':
#                # n1=int(request.GET['num1'])
#                # n2=int(request.GET['num2'])
#                n1=int(request.POST.get('num1'))
#                n2=int(request.POST.get('num2'))
#                final=n1+n2
#                url='/about-us/?output={}'.format(final)
#                return HttpResponseRedirect(url)
#      except:
#           pass
#      return render(request,'userform.html',{'output':final})

def actform(request):
     return render(request,'act-form.html')

def submitform(request):
     return HttpResponse("form submitted")

def userform(request):
     final=usersform()
     data={'form':final}
     try:
          if request.method=='POST':
               # n1=int(request.GET['num1'])
               # n2=int(request.GET['num2'])
               n1=int(request.POST.get('num1'))
               n2=int(request.POST.get('num2'))
               finalans=n1+n2
               data={'form':final,'output':finalans}

               url='/about-us/?output={}'.format(final)
               return HttpResponseRedirect(url)
     except:
          pass
     return render(request,'userform.html',data)

def calculator(request):
     c=''
     try:
          if request.method=='POST':
               n1=eval(request.POST.get('num1'))
               n2=eval(request.POST.get('num2'))
               opr=request.POST.get("opr")
               if opr=="+":
                    c=n1+n2
               elif opr=='-':
                    c=n1-n2
               elif opr=='*':
                    c=n1*n2
               elif opr=='/' :
                    c=n1/n2
               else:
                    c="error:invalid operator"
     except Exception as e:
          c=e
     return render(request,'calculator.html',{'output':c})

def evenodd(request):
     result=''
     try:
          if request.method=='POST':
               if request.POST.get('num1')=="":
                    return render(request,'evenodd.html',{'error':True})
               
               n1=int(request.POST.get('num1'))
               if n1%2==0:
                    result='Even number'
               else:
                    result='odd'
     except:
          result='Invalid'

     return render(request,'evenodd.html',{'output':result})

def marksheet(request):
     avg=''
     total=''
     d=''
     try:
          if request.method=='POST':
               sub1=int(request.POST.get('sub1'))
               sub2=int(request.POST.get('sub2'))
               sub3=int(request.POST.get('sub3'))
               sub4=int(request.POST.get('sub4'))
               sub5=int(request.POST.get('sub5'))
               total=sub1+sub2+sub3+sub4+sub5
               avg=total/5
               if avg>60:
                    d='First Division'
               elif avg>45:
                    d='second division'
               elif avg>35:
                    d='Third division'
               else:
                    d="Fail"
               
     except:
          print("error")


     return render(request,'marksheet.html',{'total':total,'avg':avg,'division':d})


     def services(request):
          serviceData=service.objects.all()
          Paginator=Paginator(serviceData,2)
          page_number=request.GET.get('page')
          servicefinalData=Paginator.get_page(page_number)
          total_pages=servicefinalData.paginator.num_pages

          data={'serviceData':servicefinalData,
                'totalpagelist':[n+1 for n in range(total_pages)]}
          return render(request,'services.html',data)
# {% if serviceData.has_previous and serviceData.has_next % }
# print("hi")
# {% endif %}
# # 
def saveEnquiry(request):
     n=''
     if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          username=request.POST.get('Username')
          password=request.POST.get('password')
          en=query(name=name,email=email,username=username,password=password)
          en.save()
          n='data saved successfully'
          
     return render(request,'contactform.html',{'n':n})
def contactform(request):
     return render(request,'contactform.html')

def img(request):
     subject='welcome to wscubetech'
     from_email='swapnil.mane23@it.sce.edu.in'
     msg='hi,this is <b> swapnil </b>'
     to_email='swapnilmane2518@gmail.com'
     msg=EmailMultiAlternatives(subject,msg,from_email,[to_email])
     msg.content_subtype='html'
     msg.send()
     # send_mail(
     #      'subject name',
     #      'message is here',
     #      'swapnil.mane23@it.sce.edu.in',
     #      ['swapnilmane2518@gmail.com'],
     #      fail_silently=False
     # )
     newsdata=news.objects.all()
     return render(request,'new.html',{'newsdata':newsdata})