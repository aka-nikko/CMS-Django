# Generated by Django 3.2.5 on 2021-08-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_articles_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='articles',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
