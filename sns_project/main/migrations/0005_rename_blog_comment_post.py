# Generated by Django 3.2 on 2021-07-12 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog',
            new_name='post',
        ),
    ]
