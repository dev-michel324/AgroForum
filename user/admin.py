from django.contrib import admin, auth
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User as UserModified

# Register your models here.

@admin.register(UserModified)
class UserModifiedAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = UserModified
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ('campos personalizados', {'fields': ('photo', 'type',)}),
    )
    add_fieldsets = auth_admin.UserAdmin.add_fieldsets + (
        (None, {'fields': ('photo','type', 'email',)}),
    )
