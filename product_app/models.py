from django.db import models

# Create your models here.


class Product(models.Model):
    class Meta:
        db_table = "product"

    name = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(null=False, default=0)
    price = models.IntegerField(null=False, default=0)


class Category(models.Model):
    class Meta:
        db_table = "category"

    name = models.CharField(max_length=100, null=True)
    parent_category_id = models.IntegerField(null=True)
    product = models.ManyToManyField(Product)
