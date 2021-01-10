from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    content = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    photo = serializers.ImageField()
    is_published = serializers.BooleanField()
    category_id = serializers.IntegerField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return News.objects.create(**validated_data)

