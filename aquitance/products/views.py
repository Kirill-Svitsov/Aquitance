from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

# from .forms import PostForm

from .models import *

num_of_pub: int = 10


def general_paginator(request, paginator):
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    template = 'products/index.html'
    products_list = Product.objects.all()
    paginator = Paginator(products_list, num_of_pub)
    page_obj = general_paginator(request, paginator)
    context = {
        'page_obj': page_obj,
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
    paginator = Paginator(all_category, num_of_pub)
    page_obj = general_paginator(request, paginator)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def category_list(request, slug):
    category_name = get_object_or_404(Category, slug=slug)
    products = category_name.products_category_related.order_by('-pub_date')
    paginator = Paginator(products, num_of_pub)
    page_obj = general_paginator(request, paginator)
    template = 'products/category_list.html'
    context = {
        'page_obj': page_obj,
        'category_name': category_name,
    }
    return render(request, template, context)


def basket(request):
    template = 'products/basket.html'
    context = {
        'text': 'Страница корзины',
    }
    return render(request, template, context)
