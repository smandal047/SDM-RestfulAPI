# Generated by Django 3.1.3 on 2020-11-27 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20201127_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='popularity',
            field=models.DecimalField(decimal_places=2, max_digits=1000),
        ),
    ]