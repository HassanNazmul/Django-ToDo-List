# Generated by Django 4.2.15 on 2024-08-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('List_API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='L', max_length=1),
        ),
    ]
