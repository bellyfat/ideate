# Generated by Django 2.0.3 on 2018-03-24 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='challenges',
            field=models.ManyToManyField(to='ideas.Challenge'),
        ),
    ]
