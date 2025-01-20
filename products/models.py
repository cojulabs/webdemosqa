from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='product_category', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title
