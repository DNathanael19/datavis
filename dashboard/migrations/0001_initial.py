# Generated by Django 4.1.6 on 2023-05-11 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeDeGoiaba',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('valor', models.FloatField(default=0)),
            ],
        ),
    ]