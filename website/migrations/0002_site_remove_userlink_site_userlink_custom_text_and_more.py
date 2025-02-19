# Generated by Django 5.1.5 on 2025-02-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userlink',
            name='site',
        ),
        migrations.AddField(
            model_name='userlink',
            name='custom_text',
            field=models.CharField(blank=True, help_text='Extra text to append to the link', max_length=50),
        ),
        migrations.AlterField(
            model_name='userlink',
            name='link',
            field=models.URLField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='userlink',
            name='sites',
            field=models.ManyToManyField(to='website.site'),
        ),
    ]
