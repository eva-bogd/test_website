# Generated by Django 4.2 on 2024-04-26 12:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0002_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='order',
            unique_together={('service', 'customer')},
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together={('name', 'esecutor')},
        ),
    ]
