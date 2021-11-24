# -*- coding: utf-8 -*-
import csv

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

import django

django.setup()

from server.member.models import Members
from server.common.models import Brand, Color
from server.cloth.models import Category
from server.cloth.models import Attribute
from server.cloth.models import Clothes
from server.cloth.constants import CLOTHES_CATEGORIES_EN_KO, CLOTHES_ATTRIBUTES_EN_KO
from server.shoppingmall.models import ShoppingMall


# def save_categories():
#     """카테고리 db에 저장"""
#     for _en_name, _ko_name in CLOTHES_CATEGORIES_EN_KO.items():
#         if 1 > Category.objects.filter(en_name=_en_name).count():
#             Category.objects.create(en_name=_en_name, ko_name=_ko_name)


# def save_attributes():
#     """속성 db에 저장"""
#     for _en_name, _ko_name in CLOTHES_ATTRIBUTES_EN_KO.items():
#         if 1 > Attribute.objects.filter(en_name=_en_name).count():
#             Attribute.objects.create(en_name=_en_name, ko_name=_ko_name)


# def save_brands():
#     return Brand.objects.create(name="chanel")


# def save_members():
#     """멤버 db에 저장"""
#     ko_member_names = ["제니", "로제", "지수", "리사", "정국", "슈가", "제이홉", "RM", "지민", "뷔", "진"]
#     en_member_names = [
#         "JENNIE",
#         "ROSE",
#         "JISOO",
#         "LISA",
#         "Jungkook",
#         "Suga",
#         "J-Hope",
#         "RM",
#         "Jimin",
#         "V",
#         "Jin",
#     ]
#     colors = [
#         "101010",
#         "F4C2C2",
#         "8057AE",
#         "FFFF66",
#         "FFFFF1",
#         "FFFFF2",
#         "FFFFF3",
#         "FFFFF4",
#         "FFFFF5",
#         "FFFFF6",
#         "FFFFF7",
#     ]
#     _brand = save_brands()

#     _group_type = "BLACKPINK"
#     for i in range(len(en_member_names)):
#         if Color.objects.filter(hex_code=colors[i]).count() < 1:
#             _color = Color.objects.create(hex_code=colors[i])
#         else:
#             _color = Color.objects.get(hex_code=colors[i])

#         if i > 3:
#             _group_type = "BTS"
#         member = Members.objects.create(
#             ko_name=ko_member_names[i],
#             en_name=en_member_names[i],
#             group_type=_group_type,
#             color=_color,
#         )


def save_lookbook_clothes():
    """룩북 의류 이미지 db에 저장"""
    member_names = {
        "V": 1,
        "JIN": 2,
        "JIMIN": 3,
        "J-HOPE": 4,
        "SUGA": 5,
        "RM": 6,
        "JUNGKOOK": 7,
    }
    _member = None
    _name = None
    i = 0
    with open("./server/lookbook_data.csv", "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        j = 1
        for line in reader:
            if line[0] in member_names:
                _name = line[0]
                if _name == 'RM':
                    _member = Members.objects.get(en_name=_name)
                else:
                    _member = Members.objects.get(en_name=_name.title())

            if line[0].isdigit():
                _image = f"lookbook/{_name}/{line[1]}.png"
                if Color.objects.filter(hex_code=line[5]).count() < 1:
                    _color = Color.objects.create(hex_code=line[5])
                else:
                    _color = Color.objects.get(hex_code=line[5])
                print(f'{i} : 브랜드 : {line[3]} category :{line[4]}')
                _category = Category.objects.get(ko_name=line[4].strip())
                if Attribute.objects.filter(ko_name=line[6]):
                    attribute1 = Attribute.objects.get(ko_name=line[6])
                else:
                    attribute1 = Attribute.objects.create(ko_name=line[6],en_name=line[6])
                if Attribute.objects.filter(ko_name=line[7]):
                    attribute2 = Attribute.objects.get(ko_name=line[7])
                else:
                    attribute2 = Attribute.objects.create(ko_name=line[7],en_name=line[7])
                if Attribute.objects.filter(ko_name=line[8]):
                    attribute3 = Attribute.objects.get(ko_name=line[8])
                else:
                    attribute3 = Attribute.objects.create(ko_name=line[8],en_name=line[8])
                
                _brand = Brand.objects.create(name=line[3])

                lookbook = Clothes.objects.create(
                    image=_image,
                    member=_member,
                    color=_color,
                    category=_category,
                )

                ShoppingMall.objects.create(cloth=lookbook, brand=_brand, price=line[9])

                _attributes = [attribute1, attribute2, attribute3]
                lookbook.attributes.set(_attributes)
                lookbook.save()
                i+=1




if __name__ == "__main__":
    save_lookbook_clothes()
