# Generated by Django 4.2.6 on 2023-10-14 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_memories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memories',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 14, 15, 4, 57, 346785)),
        ),
        migrations.AlterField(
            model_name='memories',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/memories/'),
        ),
    ]