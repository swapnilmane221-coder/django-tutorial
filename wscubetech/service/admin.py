from django.contrib import admin
from service.models import service
class serviceadmin(admin.ModelAdmin):
     list_display=['service_icon','service_title','service_description']

admin.site.register(service,serviceadmin)
# Register your models here.
