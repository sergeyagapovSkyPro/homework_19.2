from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.CharField(max_length=250, verbose_name='Слаг', **NULLABLE)
    body = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog', verbose_name='Изображение', **NULLABLE)
    create_at = models.DateTimeField(auto_created=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    view_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
