# Generated by Django 4.2.5 on 2023-09-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_bank', '0004_notemodel_username_alter_notemodel_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personmodel',
            name='phone',
            field=models.CharField(max_length=12, verbose_name='Номер телефона'),
        ),
    ]
