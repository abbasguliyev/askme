from django import forms
from account.models import User
from django.forms.widgets import PasswordInput
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
import account




class RegisterForm(forms.ModelForm):


    def _create_user(self, username, email, password1, password2, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(email=email, password1=password1, password2=password2 **extra_fields)
        
        user.password = make_password(password1)
        user.save(using=self._db)
        return user
    
    class Meta:
        model = get_user_model()
        fields = "__all__"
