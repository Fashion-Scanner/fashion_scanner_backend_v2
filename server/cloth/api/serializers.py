import json
from rest_framework import serializers
from server.cloth.models import Clothes, Attribute
from server.common.models import Color
from server.shoppingmall.models import ShoppingMall


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ["ko_name"]


class KoClothSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField("get_category_name")
    attributes = serializers.SerializerMethodField("get_attribute_name")
    brand = serializers.SerializerMethodField("get_brand_name")
    price = serializers.SerializerMethodField("get_price_name")
    
    class Meta:
        model = Clothes
        fields = [
            "image",
            "category_name",
            "attributes",
            "brand",
            "price"
        ]   

    def get_brand_name(self, obj):
        return ShoppingMall.objects.filter(cloth=obj.id).first().brand.name.title() if ShoppingMall.objects.filter(cloth=obj.id) else ""

    def get_price_name(self, obj):
        return ShoppingMall.objects.filter(cloth=obj.id).first().price if ShoppingMall.objects.filter(cloth=obj.id) else ""

    def get_category_name(self, obj):
        return obj.category.ko_name

    def get_attribute_name(self, obj):
        return [attribute.ko_name for attribute in obj.attributes.all()]


class EnClothSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField("get_en_category_name")
    attributes = serializers.SerializerMethodField("get_en_attribute_name")
    brand = serializers.SerializerMethodField("get_brand_name")
    price = serializers.SerializerMethodField("get_price_name")

    class Meta:
        model = Clothes
        fields = [
            "image",
            "category_name",
            "attributes",
            "brand",
            "price"
        ]

    def get_brand_name(self, obj):
        return ShoppingMall.objects.filter(cloth=obj.id).first().brand.name.title() if ShoppingMall.objects.filter(cloth=obj.id) else ""

    def get_price_name(self, obj):
        return ShoppingMall.objects.filter(cloth=obj.id).first().price if ShoppingMall.objects.filter(cloth=obj.id) else ""

    def get_en_category_name(self, obj):
        return obj.category.en_name.capitalize()

    def get_en_attribute_name(self, obj):
        return [attribute.en_name.replace("_", " ").title() for attribute in obj.attributes.all()]
