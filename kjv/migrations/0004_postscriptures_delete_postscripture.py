# Generated by Django 4.2.9 on 2024-02-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kjv', '0003_rename_verse_postscripture_scripture_reference'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostScriptures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('scripture_reference', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='PostScripture',
        ),
    ]
