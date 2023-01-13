# Generated by Django 4.1.5 on 2023-01-13 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TechStack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('icon_svg', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Язык п-р',
                'verbose_name_plural': 'Языки п-р',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=120)),
                ('desc_en', models.CharField(max_length=120, null=True)),
                ('desc_uk', models.CharField(max_length=120, null=True)),
                ('image', models.ImageField(upload_to='PortfolioApp/images/')),
                ('url', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('techs_tack', models.ManyToManyField(to='PortfolioApp.techstack')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
