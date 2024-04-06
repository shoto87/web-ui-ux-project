# Generated by Django 5.0.2 on 2024-04-06 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0008_alter_downloads_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]