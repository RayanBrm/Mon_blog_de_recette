# Generated by Django 3.2.13 on 2022-07-04 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_recette_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='recette',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.recette'),
        ),
    ]
