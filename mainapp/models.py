from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_lenght=128, verbose_name='Название', unique=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'#{self.pk}. {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категория'
        ordering = ('name',)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete-models.CASCADE, verbose_name='Категория')
    name = models.CrarField(max_lenght=128, verbose_name='Название')
    image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Изображение')
    short_desc = models.CharField(max_lenght=128, verbose_name='Краткое описание')
    discription = models.TextField(verbose_name='Описание')
    price = models.DecimaField(max_digits=8, decimal_placec=2, verbose_name='Цена')
    quabtity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return f'{self.name} ({self.category.name}'

    class Meta:
        verbose_name = 'продукты'
        verbose_name_plural = 'продукты'