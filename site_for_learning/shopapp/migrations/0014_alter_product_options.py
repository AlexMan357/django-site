# Generated by Django 4.2.2 on 2023-08-26 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0013_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'price'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
