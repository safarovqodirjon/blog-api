from rest_framework import serializers
from .questions import QuestionSerializer
from .image import ImageSerializer
from .tag import TagSerializer
from ..models import (Post,
                      Question,
                      Image,
                      Tag)


class PostSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=False)
    images = ImageSerializer(many=True, required=False)
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ('uuid', 'title', 'owner', 'date_modified', 'date_added', 'questions', 'images', 'tags')

    def create(self, validated_data):
        questions_data = validated_data.pop('questions', [])
        images_data = validated_data.pop('images', [])
        tags_data = validated_data.pop('tags', [])

        # Перед созданием поста извлечем и удалем теги из validated_data
        tags = tags_data.copy()
        tags_data.clear()

        post = Post.objects.create(**validated_data)

        for question_data in questions_data:
            Question.objects.create(post=post, **question_data)

        for image_data in images_data:
            Image.objects.create(post=post, **image_data)

        for tag_data in tags:
            tag = None
            if 'uuid' in tag_data:
                tag = Tag.objects.get(uuid=tag_data['uuid'])
            elif 'name' in tag_data:
                tag, _ = Tag.objects.get_or_create(name=tag_data['name'])

            if tag is not None:
                post.tags.add(tag)

        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()

        questions_data = validated_data.get('questions')
        if questions_data is not None:
            instance.questions.all().delete()

            for question_data in questions_data:
                Question.objects.create(post=instance, **question_data)

        images_data = validated_data.get('images')
        if images_data is not None:
            instance.images.all().delete()

            for image_data in images_data:
                Image.objects.create(post=instance, **image_data)

        tags_data = validated_data.get('tags')
        if tags_data is not None:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
                instance.tags.add(tag)

        return instance

    def delete(self, instance):
        instance.questions.all().delete()
        instance.images.all().delete()
        instance.tags.clear()
        instance.delete()
