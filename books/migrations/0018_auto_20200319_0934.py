# Generated by Django 3.0.4 on 2020-03-19 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_auto_20200319_0930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='journal',
            options={'verbose_name': 'book entry', 'verbose_name_plural': 'book entries'},
        ),
    ]
