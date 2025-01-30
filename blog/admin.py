from django.contrib import admin
from .models import Blog
from django.db import models
from django.forms import  Textarea

class BlogAdmin(admin.ModelAdmin):
    list_display=['author','title','text','created_date','published_date']
    list_editable=['title','text']
class TextEditorAdmin(admin.ModelAdmin):
    formfield_overrides ={ models.TextField:{'widget':Textarea()} }

admin.site.register(Blog,BlogAdmin)
#admin.site.register( TextEditorAdmin ) 

