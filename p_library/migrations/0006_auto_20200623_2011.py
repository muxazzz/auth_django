# Generated by Django 3.0.7 on 2020-06-23 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_auto_20200622_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Изображение книги'),
        ),
    ]
