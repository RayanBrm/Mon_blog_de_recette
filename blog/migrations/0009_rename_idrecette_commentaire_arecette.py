# Generated by Django 3.2.13 on 2022-07-06 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20220706_0953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentaire',
            old_name='idrecette',
            new_name='arecette',
        ),
    ]
