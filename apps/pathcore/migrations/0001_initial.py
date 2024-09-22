# Generated by Django 5.0.6 on 2024-09-21 23:49
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Corepath',
            fields=[
                (
                    'id', models.BigAutoField(
                        auto_created=True, primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name', models.CharField(
                        max_length=50,
                        verbose_name='Tronco Común',
                    ),
                ),
                ('description', models.TextField(verbose_name='Descripción')),
                ('status_delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Core',
                'db_table': 'Core',
            },
        ),
        migrations.CreateModel(
            name='CoreUser',
            fields=[
                (
                    'id', models.BigAutoField(
                        auto_created=True, primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('completed', models.BooleanField(default=False)),
                ('url_repo', models.URLField(max_length=255)),
                ('core', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pathcore.corepath',),),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,),),
            ],
            options={
                'verbose_name': 'CoreUser',
                'db_table': 'CoreUser',
            },
        ),
    ]
