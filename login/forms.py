from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import AnonymousUser
from django.core.validators import FileExtensionValidator

from login.models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    video = None

class LoginUserWithVideoForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login'}))
    password = None
    video = forms.FileField(label='Видео', required=True, widget=forms.FileInput(attrs={'class': 'form-control'}))

    def clean(self):
        username = self.cleaned_data.get("username")

        for k, v in self.request.FILES.items():
            print(k, v)

        if username is not None:
            self.user_cache = authenticate(
                self.request, username=username, video=self.request.FILES['video']
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
