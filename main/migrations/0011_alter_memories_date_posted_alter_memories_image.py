# Generated by Django 4.2.6 on 2023-10-14 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_memories_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memories',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 14, 19, 50, 55, 781881)),
        ),
        migrations.AlterField(
            model_name='memories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
