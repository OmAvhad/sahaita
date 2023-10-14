# Generated by Django 4.2.6 on 2023-10-14 12:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_medications_alter_memories_date_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicationsrecord',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='memories',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 14, 17, 59, 28, 992449)),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]