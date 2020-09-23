# Generated by Django 3.0.8 on 2020-07-22 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200722_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='blogentry',
            name='type',
        ),
        migrations.AddField(
            model_name='blogentry',
            name='images',
            field=models.ManyToManyField(blank=True, to='blog.Image'),
        ),
    ]
