from django.urls import path

from . import views

app_name = 'stores'

urlpatterns = [
    path('', views.storeListPage.as_view(), name='store_list'),
    path('create/', views.storeCreatePage.as_view(), name='store_create'),
    path('my-store/', views.myStorePage.as_view(), name='store_my_store' ),
    path('update/<slug:slug>/', views.storeUpdatePage.as_view(), name='store_update'),
    path('delete/<slug:slug>/', views.storeDeletePage.as_view(), name='store_delete'),
    path('<slug:slug>/', views.storeDetailPage.as_view(), name='store_detail'),
]
