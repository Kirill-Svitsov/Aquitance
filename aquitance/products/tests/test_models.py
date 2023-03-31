from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Category, Product, NUM_OF_WORDS

User = get_user_model()
DESCRIPTION_PRODUCT_ONE = 'Тестовый текст описания продукта с каким то количеством слов в предложении'
FIRST_TITLE_PRODUCT = 'Титульник первого продукта'
FIRST_TITLE_CATEGORY = 'Титульник первой категории'
DESCRIPTION_CATEGORY_ONE = 'Описание первой категории'
CATEGORY_SLUG = 'test-slug'
PRICE = 100


# python3 manage.py test products.tests.test_models -v2 для запуска локальных тестов
class ProductModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.category = Category.objects.create(
            title=FIRST_TITLE_CATEGORY,
            slug=CATEGORY_SLUG,
            description=DESCRIPTION_CATEGORY_ONE,
        )
        cls.product = Product.objects.create(
            author=cls.user,
            title=FIRST_TITLE_PRODUCT,
            description=DESCRIPTION_PRODUCT_ONE,
            price=PRICE,
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        fields_product_category = {
            self.product.title[:NUM_OF_WORDS]: str(self.product),
            self.category.title: str(self.category)
        }
        for key, value in fields_product_category.items():
            with self.subTest(key=key):
                self.assertEqual(key, value)

    def test_verbose_name_product(self):
        """verbose_name в полях совпадает с ожидаемым."""
        product = ProductModelTest.product
        field_verboses = {
            'title': 'Наименование товара',
            'description': 'Описание',
            'author': 'Автор',
            'category': 'Категория',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    product._meta.get_field(field).verbose_name, expected_value)

    def test_verbose_name_category(self):
        """verbose_name в полях совпадает с ожидаемым."""
        category = ProductModelTest.category
        field_verboses = {
            'title': 'Заглавие',
            'slug': 'Уникальный URL',
            'description': 'Описание',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    category._meta.get_field(field).verbose_name, expected_value)