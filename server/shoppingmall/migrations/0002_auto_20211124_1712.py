# Generated by Django 3.0.9 on 2021-11-24 17:12

from django.db import migrations, models
import django.db.models.deletion
import server.shoppingmall.models


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0003_clothes'),
        ('shoppingmall', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingmall',
            name='cloth',
        ),
        migrations.AddField(
            model_name='shoppingmall',
            name='cloth',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cloth.Clothes', verbose_name='의류'),
        ),
        migrations.AlterField(
            model_name='shoppingmall',
            name='image',
            field=models.ImageField(null=True, upload_to=server.shoppingmall.models.image_upload_to, verbose_name='쇼핑몰 의류 이미지'),
        ),
        migrations.AlterField(
            model_name='shoppingmall',
            name='url',
            field=models.TextField(null=True, verbose_name='웹 페이지 URL'),
        ),
    ]
