# Generated by Django 2.2.19 on 2023-03-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_Add_image_to_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos_category/%Y/%m/%d/', verbose_name='Изображение категории'),
        ),
    ]
