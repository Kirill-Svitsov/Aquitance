from django.contrib import admin

from .models import Product, Category


# from .models import Category

class ProductAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'title', 'pub_date', 'author', 'category')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('title', 'price')
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'title', 'description')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('title', 'description')
    empty_value_display = '-пусто-'


# класс ProductAdmin
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Category)
