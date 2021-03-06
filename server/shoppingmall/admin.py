from django.contrib import admin
from server.shoppingmall.models import ShoppingMall


class ShoppingMallAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "brand", "url", "price",)


admin.site.register(ShoppingMall, ShoppingMallAdmin)