# Generated by Django 4.2.3 on 2023-07-30 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_remove_userqaprofile_answer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='slug',
        ),
    ]
