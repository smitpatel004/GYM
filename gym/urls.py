"""
URL configuration for gym project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django import views

from gm.views import *
from django.conf.urls.static import static

from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("gm/",hame,name="hame"),
    path("gm/equipment",Equpment,name="equpment"),
    path("gm/absbegnier",absB,name="absB"),
    path("gm/chestbegnier",chestB,name="chestb"),
    path("",views.home,name="home"),
    path("gm/exe",Exe,name="Exe"),
    path("gm/login",login_page,name="login_page"),
    path("gm/register",register,name="register"),
    path("gm/logout",logout,name="logout"),
    # path("gm/register",register_page,name="register_page"),
    path("user/",views.user,name="user"),
    


    
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
