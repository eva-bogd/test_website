from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'role', 'email',
                    'phone_number')
    list_editable = ('username', 'role', 'first_name', 'role', 'email',
                     'phone_number')
    list_filter = ('role',)
    search_fields = ('username', 'email')
    empty_value_display = '-пусто-'
