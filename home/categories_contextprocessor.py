from products.models import Category
def category_filter(request):
    category_dropdown = Category.objects.all()
    return {'category_dropdown':category_dropdown}