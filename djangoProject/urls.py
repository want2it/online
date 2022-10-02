"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from price import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

admin.autodiscover()
# add a flag for
# handling the 404 error



urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('export/category/', views.CategoryExportView.as_view(), name='export-category'),
    path('', include('blog.urls')),
    path('price', include('price.urls')),
]
urlpatterns += staticfiles_urlpatterns()

handler404 = 'blog.views.error_404_view'
