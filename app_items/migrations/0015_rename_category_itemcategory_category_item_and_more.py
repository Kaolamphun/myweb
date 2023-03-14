# Generated by Django 4.1.7 on 2023-03-14 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_items', '0014_rename_category_item_itemcategory_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemcategory',
            old_name='category',
            new_name='category_item',
        ),
        migrations.RemoveField(
            model_name='itemproduct',
            name='category',
        ),
        migrations.AlterField(
            model_name='itemproduct',
            name='category_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_items.itemcategory'),
        ),
    ]