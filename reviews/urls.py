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
from . import views

app_name = 'reviews'

urlpatterns = [
    path('create/<int:id_product>/', views.ReviewCreateView.as_view(), name='review_create'),
    path('update/<int:id_product>/<int:id_review>/', views.ReviewUpdateView.as_view(), name='review_update'),
    path('delete/<int:id_product>/<int:id_review>/', views.ReviewDeleteView.as_view(), name='review_delete'),
    path('<int:id_product>/', views.ReviewListView.as_view(), name='review_list'),
    path('<int:id_product>/<slug:slug>/', views.ReviewDetailView.as_view(), name='review_detail'),
]
