from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'full_name', 'phone_number', 'email', 'password1', 'password2']