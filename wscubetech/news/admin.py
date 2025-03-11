from django.contrib import admin
from news.models import news
class newsadmin(admin.ModelAdmin):
     list_display=['news_title','news_desc','news_image']

admin.site.register(news,newsadmin)

# Register your models here.
