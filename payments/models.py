from django.db import models
from django.core import validators


class Item(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название')
    description = models.TextField(max_length=800, verbose_name='Описание')
    price = models.IntegerField(
        verbose_name='Цена',
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(100000)
        ]
    )

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name
