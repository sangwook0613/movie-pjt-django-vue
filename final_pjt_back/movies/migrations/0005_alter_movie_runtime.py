# Generated by Django 3.2.3 on 2021-05-25 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20210521_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
