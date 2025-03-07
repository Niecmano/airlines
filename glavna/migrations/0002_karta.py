# Generated by Django 5.1.4 on 2025-03-05 22:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glavna', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Karta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cena', models.DecimalField(decimal_places=2, max_digits=6)),
                ('let', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='glavna.let')),
            ],
        ),
    ]
