# Generated by Django 5.1.6 on 2025-02-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('legenda', models.CharField(max_length=150)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('foto', models.CharField(max_length=100)),
            ],
        ),
    ]
