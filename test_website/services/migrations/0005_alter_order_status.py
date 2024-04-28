# Generated by Django 4.2 on 2024-04-28 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_rename_esecutor_service_executor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('todo', 'Оформлен'), ('in_progress', 'В работе'), ('in_review', 'На проверке'), ('done', 'Выполнен')], help_text='Выберите статус заказа', max_length=11, verbose_name='Статус заказа'),
        ),
    ]
