from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import Post, Tag, Question, Image
from django.contrib.auth import get_user_model

User = get_user_model()

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag.objects.create(name='Test Tag')
        cls.user = User.objects.create(email='test@example.com', password='password')
        cls.post = Post.objects.create(
            title='Test Post',
            owner=cls.user,
            content='This is a test post.',
        )
        cls.post.tags.add(cls.tag)

    def test_title_max_length(self):
        post = Post.objects.get(uuid=self.post.uuid)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_title_label(self):
        post = Post.objects.get(uuid=self.post.uuid)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_date_modified_auto_now(self):
        old_date_modified = self.post.date_modified
        self.post.content = 'Updated content'
        self.post.save()
        new_date_modified = Post.objects.get(uuid=self.post.uuid).date_modified
        self.assertNotEqual(old_date_modified, new_date_modified)

    def test_date_added_auto_now_add(self):
        post = Post.objects.create(
            title='New Post',
            owner=self.user,
            content='This is a new post.',
        )
        self.assertIsNotNone(post.date_added)

    def test_str_method(self):
        post = Post.objects.get(uuid=self.post.uuid)
        self.assertEqual(str(post), 'Test Post')


class TagModelTest(TestCase):
    def test_tag_name_max_length(self):
        tag = Tag.objects.create(name='Test Tag')
        max_length = tag._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_tag_name_unique(self):
        tag = Tag.objects.create(name='Duplicate Tag')
        with self.assertRaises(Exception):
            Tag.objects.create(name='Duplicate Tag')


class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag.objects.create(name='Test Tag')
        cls.user = User.objects.create(email='test@example.com', password='password')
        cls.post = Post.objects.create(
            title='Test Post',
            owner=cls.user,
            content='This is a test post.',
        )
        cls.post.tags.add(cls.tag)

        cls.question = Question.objects.create(
            post=cls.post,
            question_text='Test question',
            option1='Option 1',
            option2='Option 2',
            option3='Option 3',
            option4='Option 4',
        )

    def test_question_text_max_length(self):
        question = Question.objects.get(uuid=self.question.uuid)
        max_length = question._meta.get_field('question_text').max_length
        self.assertEqual(max_length, 255)

    def test_question_str_method(self):
        question = Question.objects.get(uuid=self.question.uuid)
        self.assertEqual(str(question), 'Test question')


class ImageModelTest(TestCase):
    def test_image_title_max_length(self):
        image = Image.objects.create(title='Test Image', image=SimpleUploadedFile('test_image.jpg', b''))
        max_length = image._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_image_upload_to(self):
        upload_to = Image._meta.get_field('image').upload_to
        self.assertEqual(upload_to, 'post_images/')
