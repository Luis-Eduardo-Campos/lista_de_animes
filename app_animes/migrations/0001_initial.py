# Generated by Django 5.0.1 on 2024-04-27 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_de_anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=255)),
                ('status_de_finalizado', models.BooleanField(default=False)),
                ('resenha', models.TextField(max_length=5000)),
            ],
        ),
    ]
