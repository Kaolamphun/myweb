from django.contrib import admin
from app_items.models import ItemCategory, ItemProduct, ItemType, ItemCompany, ItemUint


# Register your models here.


# Item
class DisPlayItemAdmin(admin.ModelAdmin):
    list_display = ['name_item', 'unit_item', 'price', 'price_del', 'category_item', 'type_item', 'description', 'img_item']
    search_fields = ['name_item']
    list_filter = ['category_item', 'type_item']
admin.site.register(ItemProduct, DisPlayItemAdmin)


# Uint
class DisPlayUintAdmin(admin.ModelAdmin):
    list_display = ['uint_item']
    list_filter = ['uint_item']
admin.site.register(ItemUint, DisPlayUintAdmin)

# Category
class DisplayItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_item']
    list_filter = ['category_item']
admin.site.register(ItemCategory, DisplayItemCategoryAdmin)

# Company
class DisplayCompany(admin.ModelAdmin):
    list_display = ['company_item']
    list_filter = ['company_item']
admin.site.register(ItemCompany, DisplayCompany)

# Type
class DisplayItemTypeAdmin(admin.ModelAdmin):
    list_display = ['type_item']
    list_filter = ['type_item']
admin.site.register(ItemType, DisplayItemTypeAdmin)
