# Generated by Django 5.0.4 on 2024-05-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(verbose_name='Содержимое'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='create_at',
            field=models.DateTimeField(auto_created=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Признак публикации'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
    ]
