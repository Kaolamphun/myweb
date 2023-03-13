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
    price = models.IntegerField(null=True, blank=True, default=0)
    price_del = models.IntegerField(null=True, blank=True, default=0)
    category_item = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=True, blank=True)
    type_item = models.ForeignKey(ItemType, on_delete=models.CASCADE, blank=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    img_item = models.ImageField(max_length=55, blank=True, null=True, default="img_coming_soom.jpg")
    slug = models.SlugField(default="", null=False)
    
    def __str__(self):
        return self.category_item


    def price_group(self):
        s = '%d' % self.price
        groups = []
        while s and s[-1].isdigit():
            groups.append(s[-3:])
            s = s[:-3]
        return s + ','.join(reversed(groups))
    
    def price_del_group(self):
        s = '%d' % self.price_del
        groups = []
        while s and s[-1].isdigit():
            groups.append(s[-3:])
            s = s[:-3]
        return s + ','.join(reversed(groups))