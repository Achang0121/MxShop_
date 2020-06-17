import xadmin
from .models import VerifyCode


class VerifyCodeAdmin:
    list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
