from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import SignUpForm
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('id','email', 'is_active', 'is_superuser', 'last_login',)
    ordering = ('email',)
    model = User
    add_form = SignUpForm
    #form = CustomUserChangeForm

admin.site.register(User, CustomUserAdmin)