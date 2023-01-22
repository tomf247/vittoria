from django.test import TestCase
from http import HTTPStatus
from .models import Newsletter
from products.models import Product
from .forms import SignupForm, EditProductForm, NewsletterForm
# Create your tests here.

class RobotsTest(TestCase):
    def test_get(self):
        response = self.client.get("/robots.txt")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response["content-type"], "text/plain")
        lines = response.content.decode().splitlines()
        self.assertEqual(lines[0], "User-Agent: *")

    def test_post(self):
        response = self.client.post("/robots.txt")

        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

class SignupFormTest(TestCase):
    def test_form_validation(self):
        form = SignupForm({
            'email': 'test@example.com',
            'username': 'admin',
            'password1': 'vittoria@user',
            'password2': 'vittoria@user',
        })
        
        self.assertTrue(form.is_valid())
      
        
    def test_form_invalid_missing_email(self):
        form = SignupForm({
            'username': 'testuser',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])

class EditProductFormTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='test product',
            description='test description',
            price=10.99,
        )

    def test_form_validation(self):
        form = EditProductForm(data={'name':'test product', 'description':'test description', 'price':10.99}, instance=self.product)
        self.assertTrue(form.is_valid())
    
    def test_form_invalid_missing_name(self):
        form = EditProductForm({
            'description': 'test description',
            'price': 10.99,
        }, instance=self.product)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])

class NewsletterFormTest(TestCase):
    def test_form_validation(self):
        form = NewsletterForm({
            'emails': 'test@example.com',
        })
        self.assertTrue(form.is_valid())

    