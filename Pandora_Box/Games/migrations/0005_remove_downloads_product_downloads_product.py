# Generated by Django 5.0.3 on 2024-04-05 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0004_alter_product_product_img_alter_product_product_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downloads',
            name='product',
        ),
        migrations.AddField(
            model_name='downloads',
            name='product',
            field=models.ManyToManyField(to='Games.product'),
        ),
    ]
