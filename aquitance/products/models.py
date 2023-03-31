from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
NUM_OF_WORDS = 20


class Category(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name='Заглавие')
    image = models.ImageField(upload_to="photos_category/%Y/%m/%d/",
                              blank=True,
                              verbose_name='Изображение категории')
    slug = models.SlugField(unique=True,
                            verbose_name='Уникальный URL')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Изображение')
    title = models.CharField(max_length=30, verbose_name='Наименование товара')
    description = models.TextField(max_length=400, verbose_name='Описание', blank=True)
    price = models.IntegerField(verbose_name='Цена')
    category = models.ForeignKey(
        Category,
        related_name='products_category_related',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        help_text='Выберите группу'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products_author_related',
        verbose_name='Автор'
    )
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title[:NUM_OF_WORDS]

    class Meta:
        ordering = ("-pub_date",)
