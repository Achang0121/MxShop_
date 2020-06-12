from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render

# Create your views here.

User = get_user_model()


class CustomBackend(ModelBackend):
    """自定义用户验证"""
    
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return User
        except Exception as e:
            print(e)
            return None
