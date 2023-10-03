# Generated by Django 3.2.20 on 2023-10-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('voters', models.IntegerField()),
            ],
        ),
    ]