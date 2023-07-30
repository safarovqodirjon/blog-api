from rest_framework import serializers
from ..models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('uuid', 'name')
        read_only_fields = ('uuid',)
