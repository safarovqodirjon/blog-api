from rest_framework import serializers
from ..models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('uuid', 'name')
        read_only_fields = ('uuid',)

    def to_internal_value(self, data):
        uuid = data.get('uuid', None)
        if uuid:
            return {'uuid': uuid, 'name': ''}
        return data

    def create(self, validated_data):
        name = validated_data['name']
        tag, _ = Tag.objects.get_or_create(name=name)
        return tag
