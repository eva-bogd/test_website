from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название категории',
        help_text='Укажите название категории',
        max_length=20,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        help_text='Укажите слаг',
        max_length=20,
        unique=True,
    )

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(
        verbose_name='Название услуги',
        help_text='Укажите название услуги',
        max_length=50,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        help_text='Выберите категорию',
        on_delete=models.CASCADE,
        related_name='services'
    )
    executor = models.ForeignKey(
        User,
        verbose_name='Исполнитель',
        help_text='Укажите исполнителя',
        on_delete=models.CASCADE,
        related_name='services'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание услуги',
        blank=True,
    )
    price = models.DecimalField(
        verbose_name='Цена',
        help_text='Укажите стоимость',
        max_digits=8,
        decimal_places=2,
    )

    class Meta:
        unique_together = ['name', 'executor']

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'Оформлен'),
        ('IN_PROGRESS', 'В работе'),
        ('IN_REVIEW', 'На проверке'),
        ('DONE', 'Выполнен')
    ]

    service = models.ForeignKey(
        Service,
        verbose_name='Заказанная услуга',
        help_text='Укажите услугу',
        on_delete=models.CASCADE,
        related_name='orders',
    )
    customer = models.ForeignKey(
        User,
        verbose_name='Заказчик',
        help_text='Укажите заказчика',
        on_delete=models.CASCADE,
        related_name='orders',
    )
    status = models.CharField(
        verbose_name='Статус заказа',
        help_text='Выберите статус заказа',
        max_length=11,
        choices=STATUS_CHOICES,
    )

    class Meta:
        unique_together = ['service', 'customer']

    def __str__(self):
        return self.service.name
