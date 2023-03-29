from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('category/', views.category, name='category'),
    path('category/<slug:slug>/', views.category_list, name='category_list'),
    path('basket/', views.basket, name='basket'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    path('products/<int:product_id>/edit/', views.product_edit, name='product_edit'),
]
