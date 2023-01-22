from django.test import TestCase
from .forms import CheckoutForm
from .models import Order

class CheckoutFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'country': 'US',
            'phone': '+1234567890',
            'street_name': 'Main St',
            'apartment_name': 'Apt 1',
            'postal_code': '123456',
            'city_name': 'New York',
        }

    def test_form_valid(self):
        form = CheckoutForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_missing_name(self):
        data = self.valid_data.copy()
        data.pop('name')
        form = CheckoutForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'name': ['This field is required.']})

    def test_form_invalid_missing_email(self):
        data = self.valid_data.copy()
        data.pop('email')
        form = CheckoutForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'email': ['This field is required.']})

    def test_form_invalid_missing_phone(self):
        data = self.valid_data.copy()
        data.pop('phone')
        form = CheckoutForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'phone': ['This field is required.']})

    def test_form_invalid_missing_street_name(self):
        data = self.valid_data.copy()
        data.pop('street_name')
        form = CheckoutForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'street_name': ['This field is required.']})

    def test_form_invalid_missing_city_name(self):
        data = self.valid_data.copy()
        data.pop('city_name')
        form = CheckoutForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'city_name': ['This field is required.']})
   
    def test_form_invalid_missing_postal_code(self):
        data = self.valid_data.copy()
        data.pop('postal_code')
        form = CheckoutForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'postal_code': ['This field is required.']})

    def test_form_save(self):
        form = CheckoutForm(data=self.valid_data)
        self.assertTrue(form.is_valid())
        order = form.save()
        self.assertIsInstance(order, Order)
        self.assertEqual(order.name, self.valid_data['name'])
        self.assertEqual(order.email, self.valid_data['email'])
        self.assertEqual(order.phone, self.valid_data['phone'])
        self.assertEqual(order.street_name, self.valid_data['street_name'])
        self.assertEqual(order.apartment_name, self.valid_data['apartment_name'])
        self.assertEqual(order.postal_code, self.valid_data['postal_code'])
        self.assertEqual(order.city_name, self.valid_data['city_name'])
