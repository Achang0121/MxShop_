from random import choice

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import SmsSerializers, UserRegisterSerializers
from .models import VerifyCode
from utils.yunpian import YunPian
from MxShop.settings import YUN_PIAN_API_KEY

User = get_user_model()


class UserViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """用户注册"""
    serializer_class = UserRegisterSerializers
    queryset = User.objects.all()


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


class SmsCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """发送短信验证码"""
    serializer_class = SmsSerializers
    
    def gengrate_code(self):
        """生成4位数字验证码"""
        seeds = '1234567890'
        code = ''
        for i in range(4):
            code += choice(seeds)
        return code
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        mobile = serializer.validated_data['mobile']
        code = self.gengrate_code()
        yp = YunPian(YUN_PIAN_API_KEY)
        sms_status = yp.send_sms(code=code, mobile=mobile)
        if sms_status['code'] != 0:
            return Response({
                'mobile': sms_status['msg'],
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                'mobile': mobile,
            }, status=status.HTTP_201_CREATED)
