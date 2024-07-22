from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from contrib.users.models import User


@admin.register(User)
class MyUserAdmin(UserAdmin):
    model = User
    list_display = ( '__str__', 'first_name', 'last_name', 'email', 'is_active', 'create_time')
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'birth_date', 'avatar', 'email', 'phone', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'birth_date', 'avatar', 'email', 'phone', 'password1', 'password2',)}
        ),
        ('Permissions', {
                'fields': ('is_active', 'is_superuser', 'is_staff')
            }
        ),
    )

    search_fields = ('first_name','last_name', 'email')
    ordering = ('create_time',)
