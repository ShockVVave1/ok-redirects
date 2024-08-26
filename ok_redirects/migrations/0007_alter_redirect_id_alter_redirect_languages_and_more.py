# Generated by Django 5.0.2 on 2024-08-26 14:09

import apps.ok_redirects.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ok_redirects', '0006_auto_20220414_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirect',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='redirect',
            name='languages',
            field=apps.ok_redirects.fields.MultipleChoiceArrayField(base_field=models.CharField(blank=True, choices=[('tg', 'Tajik'), ('ru', 'Russian'), ('en', 'English')], max_length=10), blank=True, default=['tg', 'ru', 'en'], size=None, verbose_name='Languages to check redirect'),
        ),
        migrations.AlterField(
            model_name='redirect',
            name='to_language',
            field=models.CharField(blank=True, choices=[('tg', 'Tajik'), ('ru', 'Russian'), ('en', 'English')], help_text='Leave blank to redirect to the current language on the site', max_length=10, verbose_name='to language'),
        ),
    ]
