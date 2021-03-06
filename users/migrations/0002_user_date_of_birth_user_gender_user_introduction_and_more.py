# Generated by Django 4.0 on 2021-12-17 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='introduction',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='website',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
