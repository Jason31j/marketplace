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
from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    #category urls
    path('category/', views.categoryListPage.as_view(), name='category_list'),
    path('category/create/', views.categoryCreatePage.as_view(), name='category_create'),
    path('category/update/<slug:slug>/', views.categoryCreatePage.as_view(), name='category_update'),
    path('category/delete/<slug:slug>/', views.categoryDeletePage.as_view(), name='category_delete'),
    path('category/<slug:slug>/', views.categoryDetailPage.as_view(), name='category_detail'),
    #product urls
    path('', views.productListPage.as_view(), name='product_list'),
    path('create/', views.productCreatePage.as_view(), name='product_create'),
    path('update/<slug:slug>/', views.productUpdatePage.as_view(), name='product_update'),
    path('delete/<slug:slug>/', views.productDeletePage.as_view(), name='product_delete'),
    path('<slug:slug>/', views.productDetailPage.as_view(), name='product_detail'),

]
