"""
URL configuration for YourCakePage project.

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
from django.urls import path
from mycake import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('index/', views.index,name='index'),
    path('innerpage/', views.about,name='innerpage'),
    path('home', views.home,name='hero'),
    path('about/', views.about,name='about'),
    path('menu/', views.menu,name='menu'),
    path('chefs/', views.chefs,name='chefs'),
    path('gallery/', views.gallery,name='gallery'),
    path('dropdown/', views.dropdown,name='dropdown'),
    path('contact/', views.contact,name='contact'),
    path('addproduct/', views.addproduct,name='addproduct'),
    path('show/',views.show,name='show'),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    #path('token/',views.token,name='token'),
    #path('pay/',views.pay,name='pay'),
    #path('stk/',views.stk,name='stk'),
    #path('upload/',views.upload_image,name='upload'),
    #path('image/',views.show_image,name='image'),
    #path('imagedelete/<int:id>',views.imagedelete),


]