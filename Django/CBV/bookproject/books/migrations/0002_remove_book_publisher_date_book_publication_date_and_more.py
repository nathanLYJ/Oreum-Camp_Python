# Generated by Django 5.0.8 on 2024-08-12 02:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="publisher_date",
        ),
        migrations.AddField(
            model_name="book",
            name="publication_date",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="출판일"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=200, verbose_name="제목"),
        ),
    ]
