from django.db import models
from server.base.models import BaseModel

class Category(models.Model):
    ko_name = models.CharField(max_length=32, verbose_name="의류 카테고리 한국어")
    en_name = models.CharField(max_length=32, verbose_name="의류 카테고리 영어")

    def __str__(self):
        return f"{self.en_name}({self.ko_name})"

    class Meta:
        db_table = "cloth_category"
        verbose_name = "의류 카테고리"
        verbose_name_plural = "의류 카테고리"
        ordering = ["id"]

