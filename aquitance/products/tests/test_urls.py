from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from ..models import Category, Product
from .test_models import DESCRIPTION_PRODUCT_ONE, FIRST_TITLE_PRODUCT, FIRST_TITLE_CATEGORY, DESCRIPTION_CATEGORY_ONE, \
    CATEGORY_SLUG, PRICE

User = get_user_model()


# python3 manage.py test products.tests.test_urls -v2 для запуска локальных тестов

class ProductsURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='HasNoName')
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

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_url_names = {
            '/': 'products/index.html',
            f'/category/{CATEGORY_SLUG}/': 'products/category_list.html',
            '/profile/HasNoName/': 'products/profile.html',
            f'/products/{self.product.pk}/': 'products/product_detail.html',
            f'/products/{self.product.pk}/edit/': 'products/create_product.html',
            '/create/': 'products/create_product.html',
            '/category/': 'products/category.html'
        }
        for address, template in templates_url_names.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, template)

    def test_about_url_exists_at_desired_location(self):
        """Проверка доступности адреса /unexisting_page/."""
        response = self.guest_client.get('/unexisting_page/')
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_all_page_for_any_client_at_desired_location(self):
        """Страницы доступные всем пользователям."""
        url = {
            "/",
            f"/category/{CATEGORY_SLUG}/",
            "/profile/HasNoName/",
            f"/products/{self.product.pk}/",
        }
        for address in url:
            with self.subTest(address=address):
                response = self.guest_client.get(address)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_product_edit_and_create_url_exists_at_desired_location(self):
        """
            Страницы products/<int:post_id>/edit/, create/ доступны
            авторизованному пользователю.
        """
        url = {
            f'/products/{self.product.pk}/edit/',
            '/create/',
        }
        for address in url:
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertEqual(response.status_code, HTTPStatus.OK)
