from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm

from .models import *

num_of_pub: int = 9


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


def profile(request, username):
    author = get_object_or_404(User, username=username)
    products_list = author.products_author_related.order_by('-pub_date')
    paginator = Paginator(products_list, num_of_pub)
    page_obj = general_paginator(request, paginator)
    context = {
        'author': author,
        'page_obj': page_obj,
    }
    return render(request, 'products/profile.html', context)


def basket(request, username):
    author = get_object_or_404(User, username=username)
    products_list = author.products_author_related.order_by('-pub_date')
    paginator = Paginator(products_list, num_of_pub)
    page_obj = general_paginator(request, paginator)
    context = {
        'author': author,
        'page_obj': page_obj,
    }
    return render(request, 'products/basket.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        create_product = form.save(commit=False)
        create_product.author = request.user
        create_product.save()
        return redirect('products:profile', create_product.author)
    context = {
        'form': form,
    }
    return render(request, 'products/create_product.html', context)


def product_edit(request, product_id):
    edit_product = get_object_or_404(Product, pk=product_id)
    if request.user != edit_product.author:
        return redirect('products:product_detail', product_id)
    form = ProductForm(request.POST or None, instance=edit_product)
    if form.is_valid():
        form.save()
        return redirect('products:product_detail', product_id)
    context = {
        'form': form,
        'is_edit': True,
    }
    return render(request, 'products/create_product.html', context)
