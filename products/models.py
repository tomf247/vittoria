from django.db import models


GENDER_CHOICES = (
    ('M', 'MALE'),
    ('F', 'FEMALE'),
)
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Category(TimeStampedModel):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'
    def get_absolute_url(self):
        return "/categories/%s/" % self.name

class Product(TimeStampedModel):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.PROTECT)
    sku = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "/products/%s/" % self.name