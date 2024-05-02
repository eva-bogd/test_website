from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """
    Расширенная модель пользователя Django.

    Дополнительные поля:
    - role: Роль пользователя (заказчик или исполнитель).
    - phone_number: Номер телефона пользователя.
    - experience: Опыт пользователя.
    """

    CUSTOMER = 'customer'
    EXECUTOR = 'executor'

    USER_ROLE_CHOICES = [
        (CUSTOMER, 'Заказчик'),
        (EXECUTOR, 'Исполнитель')
    ]

    role = models.CharField(
        verbose_name='Роль',
        help_text='Выберите роль: заказчик/исполнитель',
        max_length=8,
        choices=USER_ROLE_CHOICES,
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        help_text='Введите адрес электронной почты',
        unique=True,
    )
    phone_number = PhoneNumberField(
        verbose_name='Номер телефона',
        help_text='Введите номер телефона',
        blank=True,
    )
    experience = models.TextField(
        verbose_name='Опыт',
        help_text='Укажите опыт',
        blank=True,
    )

    def __str__(self):
        return self.username
