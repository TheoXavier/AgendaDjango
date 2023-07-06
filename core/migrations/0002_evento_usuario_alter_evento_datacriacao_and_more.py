# Generated by Django 4.2.3 on 2023-07-05 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='dataCriacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data da criação'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='dataEvento',
            field=models.DateTimeField(verbose_name='Data do evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]
