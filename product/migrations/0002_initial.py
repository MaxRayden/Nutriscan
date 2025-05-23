# Generated by Django 5.1.6 on 2025-02-26 00:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='historicoconsulta',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='produto',
            name='ingredientes',
            field=models.ManyToManyField(related_name='produtos', to='product.ingrediente'),
        ),
        migrations.AddField(
            model_name='historicoconsulta',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.produto'),
        ),
        migrations.AddField(
            model_name='restricaoalimentar',
            name='ingredientes_perigosos',
            field=models.ManyToManyField(related_name='restricoes', to='product.ingrediente'),
        ),
        migrations.AddField(
            model_name='produto',
            name='restricoes',
            field=models.ManyToManyField(blank=True, related_name='produtos', to='product.restricaoalimentar'),
        ),
    ]
