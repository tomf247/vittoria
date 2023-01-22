class EditProductFormTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='test product',
            description='test description',
            price=10.99,
        )

    def test_form_validation(self):
        form = EditProductForm(instance=self.product)
        self.assertTrue(form.is_valid())