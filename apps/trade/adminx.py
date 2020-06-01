import xadmin
from trade.models import ShoppingCart, OrderInfo, OrderGoods


class ShoppingCartAdmin:
    list_display = ["user", "goods", "nums", ]
    model_icon = 'fa fa-shopping-cart'


class OrderInfoAdmin:
    list_display = ["user", "order_sn", "trade_no", "pay_status", "post_script", "order_mount",
                    "order_mount", "pay_time", "add_time"]
    model_icon = 'fa fa-wpforms'
    
    class OrderGoodsInline:
        model = OrderGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'
    
    inlines = [OrderGoodsInline, ]


xadmin.site.register(OrderInfo, OrderInfoAdmin)
xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
