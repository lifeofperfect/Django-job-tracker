# Generated by Django 2.2.7 on 2019-12-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acla', '0003_auto_20191203_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suspicious',
            name='comment',
            field=models.TextField(blank=True, max_length=30),
        ),
    ]