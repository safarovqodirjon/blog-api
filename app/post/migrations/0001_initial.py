# Generated by Django 4.2.3 on 2023-07-26 16:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('title', models.CharField(max_length=255)),
                ('images', models.ImageField(blank=True, null=True, upload_to='post_images/')),
                ('content', models.TextField()),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='post.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
