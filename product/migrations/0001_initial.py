# Generated by Django 3.2.6 on 2021-08-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredients', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
