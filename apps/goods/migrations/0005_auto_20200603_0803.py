# Generated by Django 2.2 on 2020-06-03 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20200601_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='goods_font_image',
            new_name='goods_front_image',
        ),
    ]
