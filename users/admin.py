from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# Register your models here.
User = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_active')

    fieldsets = (
        (None, {
            'fields': ('email', 'password', )
        }),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active',
                                    'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff',
                       'is_active')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
