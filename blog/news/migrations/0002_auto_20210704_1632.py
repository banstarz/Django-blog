# Generated by Django 3.2.4 on 2021-07-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(verbose_name='Дата'),
        ),
    ]
