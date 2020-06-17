"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from MxShop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import SmsCodeViewSet, UserViewSet

router = DefaultRouter()
# 配置goods的url
router.register(r'goods', GoodsListViewSet, basename='goods')
# 配置category的url
router.register(r'categorys', CategoryViewSet, basename='categorys')
router.register(r'codes', SmsCodeViewSet, basename='codes')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    
    # MEDIA配置
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    
    # 商品列表页
    url(r'^', include(router.urls)),
    
    url(r'docs/', include_docs_urls(title='文档')),
    
    url(r'^api-auth/', include('rest_framework.urls')),
    # drf自带的token认证接口
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt认证接口
    url(r'^login/', obtain_jwt_token),
]
