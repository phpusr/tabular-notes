# Generated by Django 3.0.1 on 2020-03-16 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_journal_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True),
        ),
    ]
