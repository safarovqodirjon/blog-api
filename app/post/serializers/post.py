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
            print(tag_data, type(tag_data))
            if isinstance(tag_data, str):
                tag_name = tag_data.strip().lower()
                tag, _ = Tag.objects.get_or_create(name=tag_name)

        post.tags.set(tags_data)

        for question_data in questions_data:
            Question.objects.create(post=post, **question_data)

        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)

        tags_data = validated_data.get('tags', [])
        tags_data_name = [item.name.strip().lower() for item in tags_data if isinstance(item.name, str)]

        tags = Tag.objects.filter(name__in=tags_data_name)

        instance.tags.set(tags)

        questions_data = validated_data.get('questions', [])
        for question_data in questions_data:
            question_uuid = question_data.get('uuid')
            if question_uuid:
                question = Question.objects.get(uuid=question_uuid)
                question.question_text = question_data.get('question_text', question.question_text)
                question.option1 = question_data.get('option1', question.option1)
                question.option2 = question_data.get('option2', question.option2)
                question.option3 = question_data.get('option3', question.option3)
                question.option4 = question_data.get('option4', question.option4)
                question.correct_option = question_data.get('correct_option', question.correct_option)
                question.save()
            else:
                Question.objects.create(post=instance, **question_data)

        instance.save()
        return instance
