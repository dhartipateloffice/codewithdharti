# Generated by Django 5.1.2 on 2024-12-01 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Codeideadb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the code snippet', max_length=255)),
                ('image', models.ImageField(blank=True, help_text='Optional image related to code', null=True, upload_to='images/')),
                ('content', models.TextField(blank=True, help_text='Optional content related to code', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Langdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('langname', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nanotopicdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nanotopic', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, help_text='Optional Output img related to code', null=True, upload_to='images/')),
                ('nano_content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NanotopicGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subtopicdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtopic', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('sub_content', models.TextField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=7, null=True)),
                ('extranote', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CodeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_content', models.TextField(help_text='Content of the code block')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('nanotopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='code_blocks', to='codewithdharti.nanotopicdb')),
            ],
        ),
        migrations.AddField(
            model_name='nanotopicdb',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nanotopics', to='codewithdharti.nanotopicgroup'),
        ),
        migrations.AddField(
            model_name='nanotopicdb',
            name='subtopic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nanotopics', to='codewithdharti.subtopicdb'),
        ),
        migrations.CreateModel(
            name='Topicdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('topic_content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('langname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='codewithdharti.langdb')),
            ],
        ),
        migrations.AddField(
            model_name='subtopicdb',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtopics', to='codewithdharti.topicdb'),
        ),
    ]