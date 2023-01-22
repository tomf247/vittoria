from django.contrib.sitemaps import Sitemap
from products import models
  
class ProductSitemap(Sitemap):
    def items(self):
        return models.Product.objects.all()
        
    def lastmod(self, obj):
        return obj.modified

class CategoriesSitemap(Sitemap):
    def items(self):
        return models.Category.objects.all()
        
    def lastmod(self, obj):
        return obj.modified