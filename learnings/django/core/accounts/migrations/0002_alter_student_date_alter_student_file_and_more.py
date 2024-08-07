# Generated by Django 4.1.5 on 2024-07-27 16:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="student",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="student",
            name="size",
            field=models.CharField(
                blank=True,
                choices=[("S", "Small"), ("M", "Medium")],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="time",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
