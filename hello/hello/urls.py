"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', view.hello),
    # url(r'^home', view.home),
    url(r'^md5', view.md5),
    # url(r'^static/(?P<path>.*)$','django.views.static.serve',),
    # url(r'^static/(?P.*)','django.views.static.serve',{'document_root': settings.STATIC_URL}),
]