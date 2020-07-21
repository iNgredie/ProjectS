from rest_framework import serializers

from .models import Ad, Tag


class AdsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ("id", "title", "price")


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


#
# class PhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ad
#         fields = "photo"
