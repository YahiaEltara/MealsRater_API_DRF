# Generated by Django 5.1.3 on 2024-11-15 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_meal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]