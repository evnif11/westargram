# Generated by Django 4.0 on 2021-12-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postings', '0002_posting_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='number_of_likes',
            field=models.IntegerField(default=0),
        ),
    ]
