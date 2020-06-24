
"""rcalltech URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('about/', views.AboutView.as_view(), name='about'),
    # path('store/', views.StoreView.as_view(),name='store'),
    path('contact/', views.ContactView.as_view(), name='contact'),

]
