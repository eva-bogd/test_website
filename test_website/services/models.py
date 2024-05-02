from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    """
    Модель категории услуг.

    Поля:
    - name: Название категории.
    - slug: Уникальный идентификатор категории для URL.
    """
    name = models.CharField(
        verbose_name='Название категории',
        help_text='Укажите название категории',
        max_length=20,
        unique=True,
    )
    slug = models.SlugField(
        verbose_name='Slug',
        help_text='Укажите slug',
        max_length=20,
        unique=True,
    )

    def __str__(self):
        return self.name


class Service(models.Model):
    """
    Модель услуги.

    Поля:
    - name: Название услуги.
    - image: Изображение, связанное с услугой.
    - category: Категория, к которой относится услуга.
    - executor: Пользователь, который является исполнителем услуги.
    - description: Описание услуги.
    - price: Цена услуги.
    """
    name = models.CharField(
        verbose_name='Название услуги',
        help_text='Укажите название услуги',
        max_length=50,
    )
    image = models.ImageField(
        verbose_name='Изображение',
        help_text='Загрузите изображение',
        upload_to='services/',
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        help_text='Выберите категорию',
        null=True,
        on_delete=models.SET_NULL,
        related_name='services'
    )
    executor = models.ForeignKey(
        User,
        verbose_name='Исполнитель',
        help_text='Укажите исполнителя',
        null=True,
        on_delete=models.SET_NULL,
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

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Модель заказа услуги.

    Поля:
    - service: Услуга, на которую оформлен заказ.
    - name: Название заказанной услуги.
    - description: Описание заказанной услуги.
    - price: Цена заказанной услуги.
    - executor: Пользователь, который является исполнителем заказа.
    - customer: Пользователь, который является заказчиком.
    - status: Статус заказа.
    """
    STATUS_CHOICES = [
        ('TODO', 'Оформлен'),
        ('IN_PROGRESS', 'В работе'),
        ('IN_REVIEW', 'На проверке'),
        ('TO_FIX', 'На доработку'),
        ('DONE', 'Выполнен'),
        ('CANCEL', 'Отменен')
    ]

    service = models.ForeignKey(
        Service,
        verbose_name='Заказанная услуга',
        help_text='Укажите услугу',
        null=True,
        on_delete=models.SET_NULL,
        related_name='orders',
    )
    name = models.CharField(
        verbose_name='Название услуги',
        help_text='Укажите название услуги',
        max_length=50,
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
    executor = models.ForeignKey(
        User,
        verbose_name='Исполнитель',
        help_text='Укажите исполнителя',
        null=True,
        on_delete=models.SET_NULL,
        related_name='executor_orders'
    )
    customer = models.ForeignKey(
        User,
        verbose_name='Заказчик',
        help_text='Укажите заказчика',
        null=True,
        on_delete=models.SET_NULL,
        related_name='customer_orders',
    )
    status = models.CharField(
        verbose_name='Статус заказа',
        help_text='Выберите статус заказа',
        max_length=11,
        choices=STATUS_CHOICES,
    )

    def __str__(self):
        return self.order.name
