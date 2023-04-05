# Generated by Django 4.2 on 2023-04-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Введите автора книги', to='catalog.author', verbose_name='Автор книги'),
        ),
    ]