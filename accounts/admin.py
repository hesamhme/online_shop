from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    model = get_user_model()
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ('email', 'username', )
