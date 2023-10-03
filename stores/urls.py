"""
URL configuration for Marketplace project.

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
from . import views

app_name = 'stores'

urlpatterns = [
    path('', views.storeListPage.as_view(), name='store_list'),
    path('<slug:slug>/', views.storeDetailPage.as_view(), name='store_detail'),
    path('create/', views.storeCreatePage.as_view(), name='store_create'),
    path('<slug:slug>/update/', views.storeUpdatePage.as_view(), name='store_update'),
    path('search/', views.storeSearchPage.as_view(), name='store_search'),
    path('<slug:slug>/delete/', views.storeDeletePage.as_view(), name='store_delete'),

]
