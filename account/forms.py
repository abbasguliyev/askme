from django import forms
from account.models import User
from django.forms.widgets import PasswordInput
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
import account

# class RegisterForm(forms.ModelForm):


#     def _create_user(self, username, email, password1, password2, **extra_fields):
#         if not username:
#             raise ValueError("The given username must be set")
#         email = self.normalize_email(email)
#         # Lookup the real model class from the global app registry so this
#         # manager method can be used in migrations. This is fine because
#         # managers are by definition working on the real model.
#         user = self.model(email=email, password1=password1, password2=password2 **extra_fields)
        
#         user.password = make_password(password1)
#         user.save(using=self._db)
#         return user
    
#     class Meta:
#         model = get_user_model()
#         fields = "__all__"

"""
1. password1 ve password2 bizim modelde yoxdur, ona gore de onlari ozumuz elave edirik, fields hissesinde de
djangonun default password fieldini qeyd etmirik. 
2. clean metodu ile validasiyamizi edirik, bunu clean-siz de etmek olar amma en dogru uslub validasiyalari clean()
metodu icerisinde etmekdir. Orda da kodlari oxusan gorersenki eslinde cox sadedir anlasilandir,
password1 ve password2-nin eyni olub olmamasi yoxlanilir, eger eyni deyilse ValidationError verir.
eks halda ise cleaned_data-ni return edir. clean_data ise formdan gelen datalari saxlayan bir dictionarydir.
3. save metodu ile ise bizim formdan gelen datalari saxlayiriq ve user obyektini yaradir
 ve user obyektini save edirik.
"""

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match!")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
