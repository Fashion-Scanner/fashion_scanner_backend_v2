from django.conf import settings
from django.urls import include, path
from server.cloth.api.views import ClothViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("cloth", ClothViewSet, basename="cloth")

app_name = "api"
urlpatterns = router.urls
