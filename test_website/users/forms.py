from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

User = get_user_model()


class CreationForm(UserCreationForm):
    """
    Форма регистрации нового пользователя.
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'role', 'email')


class ProfileUpdateForm(forms.ModelForm):
    """
    Форма обновления профиля пользователя.
    """
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'role',
            'email',
            'phone_number',
            'experience'
            )


class PasswordChangingForm(PasswordChangeForm):
    """
    Форма сменя пароля.
    """
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
