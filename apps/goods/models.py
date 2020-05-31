from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


class GoodsCategory(models.Model):
    """商品分类"""
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    name = models.CharField(max_length=30, default="", verbose_name="类别名", help_text="类别名")
    code = models.CharField(max_length=30, default="", verbose_name="类别code", help_text="类别code")
    desc = models.CharField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.CharField(choices=CATEGORY_TYPE, default=1, verbose_name="类别类型", help_text="类别类型")
    parent_category = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="sub_cat",
        verbose_name="父类别",
        help_text="父类别",
    )
    is_tab = models.BooleanField(default=False, verbose_name="是否在导航栏", help_text="是否在导航栏")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """品牌名"""
    category = models.ForeignKey(
        GoodsCategory,
        related_name='brands',
        null=True, blank=True,
        verbose_name="商品类目",
        on_delete=models.CASCADE,
    )
    name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
    desc = models.TextField(default="", max_length=200, verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brands/", verbose_name="品牌图片")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name


class Goods(models.Model):
    """商品"""
    category = models.ForeignKey(GoodsCategory, verbose_name="商品类目", on_delete=models.CASCADE)
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
    name = models.CharField(max_length=100, verbose_name="商品名")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    sold_nums = models.IntegerField(default=0, verbose_name="商品销售量")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    goods_nums = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    shop_price = models.FloatField(default=0, verbose_name="本店价格")
    goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")
    goods_desc = UEditorField(
        verbose_name=u"内容",
        imagePath="goods/images/",
        width=1000,
        height=300,
        filePath="goods/files/",
        default='',
    )
    is_ship_free = models.BooleanField(default=True, verbose_name="是否免运费")
    goods_font_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """商品轮播图"""
    goods = models.ForeignKey(Goods, verbose_name="商品", related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """轮播商品"""
    goods = models.ForeignKey(Goods, verbose_name="商品", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner/', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播图顺序索引")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
    class Meta:
        verbose_name = "商品商品"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.goods.name
