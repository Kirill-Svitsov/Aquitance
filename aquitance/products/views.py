from django.shortcuts import get_object_or_404, redirect, render

from .models import *


def index(request):
    template = 'products/index.html'
    products = Product.objects.order_by('-pub_date')[:10]
    context = {
        'products': products,
    }
    return render(request, template, context)


def product_detail(request):
    template = 'products/product_detail.html'
    context = {
        'text': 'Детали товара',
    }
    return render(request, template, context)


def category(request):
    template = 'products/category.html'
    all_category = Category.objects.all()
    context = {
        'all_category': all_category,
    }
    return render(request, template, context)


def category_list(request, slug):
    category_name = get_object_or_404(Category, slug=slug)
    products = category_name.products_category_related.order_by('-pub_date')
    template = 'products/category_list.html'
    context = {
        'products': products,
        'category_name': category_name,
    }
    return render(request, template, context)


def basket(request):
    template = 'products/basket.html'
    context = {
        'text': 'Страница корзины',
    }
    return render(request, template, context)
