from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('category/', views.category, name='category'),
    path('category/<slug:slug>/', views.category_list, name='category_list'),
    path('basket/', views.basket, name='basket'),
]
