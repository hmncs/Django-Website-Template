# Generated by Django 3.1.7 on 2021-03-14 07:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0003_remove_question_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_answer',
            field=tinymce.models.HTMLField(default=''),
            preserve_default=False,
        ),
    ]
