# Generated by Django 4.1.5 on 2023-01-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0003_remove_project_techs_tack_project_techs_tack'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='techstack',
            options={'verbose_name': 'Язык п-р', 'verbose_name_plural': 'Языки п-р'},
        ),
        migrations.AddField(
            model_name='techstack',
            name='icon_svg',
            field=models.TextField(default='fasaf'),
            preserve_default=False,
        ),
    ]