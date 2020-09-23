# Generated by Django 3.0.8 on 2020-07-22 18:01

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0002_blogentry_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='type',
            field=models.CharField(choices=[('#eee', 'grow'), ('#EA00A3', 'note')], default='#eee', max_length=24),
        ),
    ]
