# Generated by Django 4.2.7 on 2023-11-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.png', upload_to='user_images', verbose_name='Фото профілю'),
        ),
    ]
