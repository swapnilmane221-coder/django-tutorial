from django.contrib import admin
from contactquery.models import query
from contactquery.models import msg
class queryadmin(admin.ModelAdmin):
     list_display=['name','email','username','password']
class msgadmin(admin.ModelAdmin):
     list_display=['message']
admin.site.register(msg,msgadmin)
admin.site.register(query,queryadmin)
# Register your models here.
