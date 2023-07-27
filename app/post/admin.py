from django.contrib import admin
from .models import Post, Tag, Question, Image, UserQAProfile


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', "owner", 'date_modified', 'date_added')
    inlines = [QuestionInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('post', 'question_text', 'option1', 'option2', 'option3', 'option4')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


@admin.register(UserQAProfile)
class UserQAProfileAdmin(admin.ModelAdmin):
    list_display = ("uuid",)
