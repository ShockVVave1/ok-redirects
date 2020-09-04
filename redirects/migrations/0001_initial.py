# Generated by Django 2.2 on 2020-09-03 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redirect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_path', models.CharField(db_index=True, help_text="This should be an absolute path, excluding the domain name. Example: '/events/search/'.", max_length=250, verbose_name='redirect from')),
                ('is_ignore_get_params', models.BooleanField(default=True, verbose_name='Ignore GET parameters')),
                ('new_path', models.CharField(blank=True, help_text="This can be either an absolute path (as above) or a full URL starting with 'http://'.", max_length=250, verbose_name='redirect to')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'redirect',
                'verbose_name_plural': 'redirects',
                'db_table': 'django_redirect',
                'ordering': ('old_path',),
                'unique_together': {('site', 'old_path')},
            },
        ),
    ]
