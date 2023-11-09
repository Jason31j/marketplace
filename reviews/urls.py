from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    path('create/<int:id_product>/', views.ReviewCreateView.as_view(), name='review_create'),
    path('update/<int:id_review>/', views.ReviewUpdateView.as_view(), name='review_update'),
    path('delete/<int:id_review>/', views.ReviewDeleteView.as_view(), name='review_delete'),
    path('<int:id_product>/', views.ReviewListView.as_view(), name='review_list'),
]
