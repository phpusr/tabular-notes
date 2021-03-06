# Generated by Django 2.2.4 on 2019-10-15 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tv_series', '0016_auto_20191012_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_name', models.CharField(max_length=100)),
                ('original_name', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('local_name', 'original_name')},
            },
        ),
        migrations.AddField(
            model_name='journal',
            name='tv_series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tv_series.TVSeries'),
        ),
        migrations.AlterUniqueTogether(
            name='journal',
            unique_together={('owner', 'tv_series')},
        ),
    ]
