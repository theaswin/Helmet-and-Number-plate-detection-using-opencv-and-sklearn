# Generated by Django 2.2.12 on 2023-01-27 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Detection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='Image',
            field=models.FileField(upload_to='Input/data'),
        ),
    ]