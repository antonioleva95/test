from django.contrib import admin
from myapp.models import content




class new_content(admin.ModelAdmin):
    list_display=['name','description','country','cost','count', 'img']
admin.site.register(content, new_content)
# Register your models here.
