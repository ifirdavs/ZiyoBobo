# Generated by Django 4.1.4 on 2022-12-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yangilik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=100)),
                ('sarlavha_en', models.CharField(max_length=100, null=True)),
                ('sarlavha_ru', models.CharField(max_length=100, null=True)),
                ('sarlavha_uz_latn', models.CharField(max_length=100, null=True)),
                ('sarlavha_uz_cyrl', models.CharField(max_length=100, null=True)),
                ('sana', models.DateField(auto_now_add=True)),
                ('matn', models.TextField()),
                ('matn_en', models.TextField(null=True)),
                ('matn_ru', models.TextField(null=True)),
                ('matn_uz_latn', models.TextField(null=True)),
                ('matn_uz_cyrl', models.TextField(null=True)),
                ('rasm', models.FileField(blank=True, null=True, upload_to='')),
                ('korish_soni', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
