from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    # product reviews urls
    path('product/create/<int:id_product>/', views.ReviewProductCreateView.as_view(), name='review_product_create'),
    path('product/update/<int:id_review>/', views.ReviewProductUpdateView.as_view(), name='review_product_update'),
    path('product/delete/<int:id_review>/', views.ReviewProductDeleteView.as_view(), name='review_product_delete'),
    path('product/<int:id_product>/', views.ReviewProductListView.as_view(), name='review_product_list'),
    # store reviews urls
    path('store/create/<int:id_store>/', views.ReviewStoreCreateView.as_view(), name='review_store_create'),
    path('store/update/<int:id_review>/', views.ReviewStoreUpdateView.as_view(), name='review_store_update'),
    path('store/delete/<int:id_review>/', views.ReviewStoreDeleteView.as_view(), name='review_store_delete'),
    path('store/<int:id_store>/', views.ReviewStoreListView.as_view(), name='review_store_list'),

]
