# Generated by Django 4.2.6 on 2023-10-14 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_memories_date_posted_alter_memories_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memories',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 14, 16, 19, 17, 531985)),
        ),
        migrations.AlterField(
            model_name='memories',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]