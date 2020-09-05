from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (
            None, {
                'fields': ('email', 'password')
            }
        ),
        ('personal Info', {
            'fields': ('name',)

        }),
        ('permissions', {
            'fields': ('is_active', 'is_superuser')
        }),
        ('Important Dates', {
            'fields': ('last_login',)

        })

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(User, UserAdmin)
