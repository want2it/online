from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on')
    list_filter = ("status", 'created_on', 'title')
    summernote_fields = ('content')
    search_fields = ['title', 'content', 'status', 'created_on']
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post, PostAdmin)





