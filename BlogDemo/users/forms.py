# -*- coding: utf-8 -*-
# @Time    : 2017/9/10 23:13
# @Author  : yj

from django.contrib.auth.forms import UserCreationForm

from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")