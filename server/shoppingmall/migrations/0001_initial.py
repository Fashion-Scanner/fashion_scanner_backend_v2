# Generated by Django 3.0.9 on 2021-10-16 07:29

from django.db import migrations, models
import django.db.models.deletion
import server.shoppingmall.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0004_auto_20211016_0605'),
        ('cloth', '0003_clothes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingMall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='Primary ID')),
                ('createdAt', models.DateTimeField(null=True)),
                ('updatedAt', models.DateTimeField(null=True)),
                ('image', models.ImageField(upload_to=server.shoppingmall.models.image_upload_to, verbose_name='쇼핑몰 의류 이미지')),
                ('url', models.TextField(verbose_name='웹 페이지 URL')),
                ('price', models.IntegerField(default=0, verbose_name='가격')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Brand', verbose_name='브랜드')),
                ('cloth', models.ManyToManyField(to='cloth.Clothes', verbose_name='의류')),
            ],
            options={
                'verbose_name': '쇼핑몰',
                'verbose_name_plural': '쇼핑몰',
                'db_table': 'shoppingmall_shoppingmall',
                'ordering': ['id'],
            },
        ),
    ]
