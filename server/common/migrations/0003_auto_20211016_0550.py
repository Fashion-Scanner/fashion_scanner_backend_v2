# Generated by Django 3.0.9 on 2021-10-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20211016_0537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='Primary ID')),
                ('createdAt', models.DateTimeField(null=True)),
                ('updatedAt', models.DateTimeField(null=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='브랜드')),
            ],
            options={
                'verbose_name': '색상',
                'verbose_name_plural': '색상',
                'db_table': 'common_brand',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelTable(
            name='color',
            table='common_color',
        ),
    ]
