# Generated by Django 4.2.7 on 2023-11-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('Повний пакет', 'full'), ('Безкоштовний пакет', 'free')], default='Безкоштовний пакет', max_length=30),
        ),
    ]