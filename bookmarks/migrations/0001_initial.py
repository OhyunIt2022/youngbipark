# Generated by Django 3.2.14 on 2022-08-02 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='북마크 이름')),
                ('url', models.URLField(verbose_name='URL')),
                ('memo', models.TextField(verbose_name='메모')),
            ],
        ),
    ]
