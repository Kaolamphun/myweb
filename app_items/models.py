from django.db import models


# Create your models here.
# models sent to views in app_base

class ItemCategory(models.Model):
    category_item = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.category_item


class ItemType(models.Model):
    type_item = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.type_item


class ItemCompany(models.Model):
    company_item = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.company_item


class ItemUint(models.Model):
    uint_item = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.uint_item


class ItemProduct(models.Model):
    name_item = models.CharField(max_length=55)
    dosage_item = models.CharField(max_length=55, null=True, blank=True)
    unit_item = models.ForeignKey(ItemUint, on_delete=models.CharField, null=True, blank=True)
    size_item = models.CharField(max_length=55, null=True, blank=True)
    company_item = models.ForeignKey(ItemCompany, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    price_del = models.IntegerField(null=True, blank=True)
    category_item = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=True, blank=True)
    type_item = models.ForeignKey(ItemType, on_delete=models.CASCADE, blank=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    img_item = models.ImageField(max_length=55, blank=True, null=True)
