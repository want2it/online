# Generated by Django 4.1 on 2022-09-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='http://127.0.0.1:8000/media/django-summernote/2022-09-17/fafea17e-9d29-42d6-8d6a-7eaf6d03017e.jpg'),
        ),
    ]
