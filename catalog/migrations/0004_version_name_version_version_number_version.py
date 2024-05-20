# Generated by Django 5.0.4 on 2024-05-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='version',
            name='name_version',
            field=models.CharField(default=None, max_length=250, verbose_name='Имя версии'),
        ),
        migrations.AddField(
            model_name='version',
            name='number_version',
            field=models.IntegerField(default=1, verbose_name='Номер версии'),
        ),
    ]
