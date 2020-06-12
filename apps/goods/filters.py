from django.db.models.base import Q

from django_filters import rest_framework as filters

from .models import Goods


class GoodsFilter(filters.FilterSet):
    """商品过滤类"""
    pricemin = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    pricemax = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    top_category = filters.NumberFilter(method='top_category_filter')
    
    def top_category_filter(self, queryset, name, value):
        queryset = queryset.filter(
            Q(category_id=value) |
            Q(category__parent_category_id=value) |
            Q(category__parent_category__parent_category_id=value)
        )
        return queryset
    
    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'name']
