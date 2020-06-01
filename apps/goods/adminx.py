import xadmin
from goods.models import GoodsImage, Goods, GoodsCategory, Banner, GoodsCategoryBrand


class GlobalSettings:
    site_title = "MxShop后台管理系统"
    site_footer = "MxShop"
    menu_style = "accordion"


class BaseSettings:
    # 主题修改
    enable_themes = True
    use_bootswatch = True


class GoodsAdmin:
    list_display = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop_price", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time"]
    search_fields = ['name', ]
    list_editable = ["is_hot", ]
    list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                   "shop_price", "is_new", "is_hot", "add_time", "category__name"]
    style_fields = {"goods_desc": "ueditor"}
    model_icon = 'fa fa-product-hunt'
    
    class GoodsImagesInline:
        model = GoodsImage
        exclude = ["add_time"]
        extra = 1
        style = 'tab'
    
    inlines = [GoodsImagesInline]


class GoodsCategoryAdmin:
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', ]
    model_icon = 'fa fa-list-alt'


class GoodsBrandAdmin:
    list_display = ["category", "image", "name", "desc"]
    model_icon = 'fa fa-anchor'
    
    def get_context(self):
        context = super(GoodsBrandAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = GoodsCategory.objects.filter(category_type=1)
        return context


class BannerGoodsAdmin:
    list_display = ["goods", "image", "index"]
    model_icon = 'fa fa-spinner fa-spin'


class HotSearchAdmin(object):
    list_display = ["keywords", "index", "add_time"]


class IndexAdAdmin(object):
    list_display = ["category", "goods"]


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(Banner, BannerGoodsAdmin)
xadmin.site.register(GoodsCategoryBrand, GoodsBrandAdmin)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
