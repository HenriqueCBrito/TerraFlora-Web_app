# Generated by Django 5.1.2 on 2024-11-25 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("farm", "0003_delete_task"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Event",
        ),
    ]