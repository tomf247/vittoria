from django.db import models

# Create your models here.

class Newsletter(models.Model):
    emails = models.EmailField(null=True,blank=True,unique=True)
    def __str__(self):
        return self.emails