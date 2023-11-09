from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    #category urls
    path('category/', views.categoryListPage.as_view(), name='category_list'),
    path('category/create/', views.categoryCreatePage.as_view(), name='category_create'),
    path('category/update/<slug:slug>/', views.categoryUpdatePage.as_view(), name='category_update'),
    path('category/delete/<slug:slug>/', views.categoryDeletePage.as_view(), name='category_delete'),
    
    #product urls
    path('create/', views.productCreatePage.as_view(), name='product_create'),
    path('update/<slug:slug>/', views.productUpdatePage.as_view(), name='product_update'),
    path('delete/<slug:slug>/', views.productDeletePage.as_view(), name='product_delete'),
    path('<str:category>/<slug:slug>/', views.productDetailPage.as_view(), name='product_detail'),
    path('<str:category>/', views.productListPage.as_view(), name='product_list'),

]
