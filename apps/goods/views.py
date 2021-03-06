from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication

from .serializers import GoodsSerializer, CategorySerializer
from .models import Goods, GoodsCategory
from .filters import GoodsFilter


class GoodsPagination(PageNumberPagination):
    """分页"""
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """商品列表页，分页、搜索、过滤、排序"""
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
        
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
    


