# Generated by Django 3.2.13 on 2022-07-05 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_ingredient_recette'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membre',
            name='mdp',
        ),
    ]
