from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['date_release', 'head']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['message_body'] 


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title'] 

