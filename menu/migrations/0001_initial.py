# Generated by Django 3.2.7 on 2021-09-27 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контент',
                'db_table': 'content',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_content', models.TextField(verbose_name='Тексты')),
            ],
            options={
                'verbose_name': 'Содержание страницы',
                'verbose_name_plural': 'Содержание страниц',
                'db_table': 'page_content',
            },
        ),
        migrations.CreateModel(
            name='StaticPages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название страницы')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка на страницу')),
                ('content', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.content')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.staticpages')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'db_table': 'static_pages',
            },
        ),
        migrations.AddField(
            model_name='content',
            name='text',
            field=models.ManyToManyField(to='menu.PageContent'),
        ),
    ]
