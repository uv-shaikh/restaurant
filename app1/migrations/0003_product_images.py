# Generated by Django 3.2.9 on 2021-11-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20211114_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, upload_to='pro_img'),
        ),
    ]
