# Generated by Django 5.0.8 on 2024-08-12 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="제목")),
                ("author", models.CharField(max_length=100, verbose_name="저자")),
                ("publisher_date", models.DateField(verbose_name="출판사")),
            ],
            options={
                "verbose_name": "도서",
                "verbose_name_plural": "도서들",
            },
        ),
    ]
