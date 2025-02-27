# Generated by Django 5.1.1 on 2024-10-09 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_product_packet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='profit',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]
