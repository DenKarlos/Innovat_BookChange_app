# Generated by Django 4.2.3 on 2023-07-31 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=100, verbose_name='название жанра')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='название книги')),
                ('authors', models.CharField(blank=True, max_length=200, null=True, verbose_name='авторы')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='описание')),
                ('language', models.CharField(blank=True, max_length=100, null=True, verbose_name='язык')),
                ('publication_year', models.IntegerField(blank=True, null=True, verbose_name='год публикации')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='время добавления')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('photo', models.ImageField(blank=True, upload_to='book_photo/', verbose_name='фотография книги')),
                ('genre', models.ManyToManyField(blank=True, related_name='books', to='books.genre')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['title'],
            },
        ),
    ]
