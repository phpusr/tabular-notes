# Generated by Django 2.2.4 on 2019-10-12 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20191012_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
