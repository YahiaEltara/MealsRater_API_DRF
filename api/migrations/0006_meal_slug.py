# Generated by Django 5.1.3 on 2024-11-16 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_meal_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]