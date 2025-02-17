from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import get_user_model

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',"password")
    class meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "password1", "password2"]

admin.site.register(get_user_model(), UserAdmin)



