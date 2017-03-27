"""zoo_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
<<<<<<< HEAD
from main.zoo import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^zoo/', include('main.zoo.urls')),
=======
from main.zoo import urls as zoo_urls
from .views import HomePage

urlpatterns = [
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^zoo/', include(zoo_urls, namespace='zoo')),
>>>>>>> 5b9301df6434630a9866467f25e3b4026750e4c4
    url(r'^admin/', admin.site.urls),
]
