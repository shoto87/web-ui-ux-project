# Generated by Django 5.0.3 on 2024-04-05 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0007_alter_downloads_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloads',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
