from django.contrib import admin
from django.utils.html import format_html

from .models import Post, Tag, Question, Image, UserQAProfile


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'title', 'owner', 'date_modified', 'date_added', 'preview_images')
    list_filter = ('owner',)
    search_fields = ('title', 'owner__username')
    readonly_fields = ('uuid',)
    inlines = [QuestionInline]

    def preview_images(self, obj):
        images = obj.images.all()[:2]
        previews = [f'<img src="{image.image.url}" height="50" />' for image in images]
        return format_html(' '.join(previews))

    preview_images.short_description = 'Preview Images'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('post', 'question_text', 'option1', 'option2', 'option3', 'option4')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview')

    def preview(self, obj):
        return format_html('<img src="{}" height="50" />', obj.image.url)

    preview.short_description = 'Preview'


@admin.register(UserQAProfile)
class UserQAProfileForm(admin.ModelAdmin):
    class Meta:
        model = UserQAProfile
        fields = ('uuid',)
