"""
URL configuration for comparing_template project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from register import views, homepage_view

from viewlist.views import ProductList

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('product_list/', ProductList.as_view()),
    path("home/", homepage_view, name="homepage"),
]
