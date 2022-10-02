from django.views.generic.list import ListView
from import_export import mixins
from . import models
from django.shortcuts import render
from django.template import RequestContext
from django.views import generic
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from .models import Book
from blog.models import Post
from django.http import Http404
from django.http import HttpResponse


class CategoryExportView(mixins.ExportViewFormMixin, ListView):
    model = models.Category


class BookListPrice(generic.ListView):
    queryset = Book.objects.order_by('id')
    template_name = 'category_list.html'

class PostListPrice(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'price.html'
