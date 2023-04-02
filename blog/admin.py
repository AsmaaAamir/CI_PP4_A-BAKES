from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredient_content', 'instruction_content')
  


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']