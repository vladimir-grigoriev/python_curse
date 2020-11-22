from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper

class RegistrationUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.base_fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        self.base_fields['username'].widget.attrs.update({'placeholder': 'Login'})
        self.base_fields['email'].widget.attrs.update({'placeholder': 'Enter email'})
        self.base_fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.base_fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
