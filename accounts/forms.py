from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class UserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', )


class UserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', )
