# Generated by Django 3.0.3 on 2020-02-16 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='book_review',
        ),
    ]