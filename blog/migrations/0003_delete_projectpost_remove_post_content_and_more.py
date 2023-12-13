# Generated by Django 5.0 on 2023-12-12 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_award_projectpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectPost',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='project_type',
            field=models.CharField(default='general', max_length=100),
        ),
    ]
