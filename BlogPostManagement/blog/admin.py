from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','content', 'category','tag')
admin.site.register(Blog, BlogAdmin)