# Generated by Django 5.0.2 on 2024-02-27 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
