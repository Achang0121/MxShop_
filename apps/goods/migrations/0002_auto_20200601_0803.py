# Generated by Django 2.2 on 2020-06-01 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='click_nums',
            new_name='click_num',
        ),
        migrations.RenameField(
            model_name='goods',
            old_name='fav_nums',
            new_name='fav_num',
        ),
        migrations.RenameField(
            model_name='goods',
            old_name='goods_nums',
            new_name='goods_num',
        ),
        migrations.RenameField(
            model_name='goods',
            old_name='sold_nums',
            new_name='sold_num',
        ),
    ]
