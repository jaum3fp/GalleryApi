# Generated by Django 4.2.7 on 2024-01-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtApi', '0007_alter_artwork_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(default=None, upload_to='static/'),
        ),
    ]
