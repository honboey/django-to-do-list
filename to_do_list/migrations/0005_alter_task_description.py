# Generated by Django 4.2.5 on 2023-09-11 00:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("to_do_list", "0004_alter_task_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
