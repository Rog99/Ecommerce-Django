# Generated by Django 4.0.1 on 2022-01-30 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_product_id_producttags_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttags',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='get_product', to='products.productdetails'),
        ),
    ]
