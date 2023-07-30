from rest_framework import serializers
from .questions import QuestionSerializer
from .image import ImageSerializer
from .tag import TagSerializer
from ..models import (Post, Question, Image, Tag)


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, required=False, slug_field="name",
                                        queryset=Tag.objects.filter())
    images = ImageSerializer(many=True, required=False)
    questions = QuestionSerializer(many=True, required=False)

    class Meta:
        model = Post
        read_only_fields = ('owner',)
        fields = ("uuid", "title", "content", "owner", "images", "tags", "questions", "date_modified", "date_added",)

    def to_internal_value(self, data):
        tags_data = data.get('tags', [])

        for tag_data in tags_data:
            if isinstance(tag_data, str):
                tag_name = tag_data.strip().lower()
                Tag.objects.get_or_create(name=tag_name)

        return super().to_internal_value(data)

    def create(self, validated_data):
        questions_data = validated_data.pop('questions', [])
        tags_data = validated_data.pop('tags', [])

        post = Post.objects.create(**validated_data)

        for tag_data in tags_data:
            if isinstance(tag_data, str):
                tag_name = tag_data.strip().lower()
                tag, _ = Tag.objects.get_or_create(name=tag_name)

        post.tags.set(tags_data)

        for question_data in questions_data:
            Question.objects.create(post=post, **question_data)

        return post
