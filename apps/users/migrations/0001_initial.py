# Generated by Django 5.0.6 on 2024-07-20 19:18
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # noqa: E501
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),  # noqa: E501
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electrónico')),  # noqa: E501
                ('name', models.CharField(verbose_name='Nombre')),
                ('last_name', models.CharField(verbose_name='Apellido')),
                ('is_partner', models.BooleanField(default=False, verbose_name='Es colaborador')),  # noqa: E501
                ('is_active', models.BooleanField(default=True, verbose_name='Está activo')),  # noqa: E501
                ('is_staff', models.BooleanField(default=False, verbose_name='Es staff')),  # noqa: E501
                ('is_superadmin', models.BooleanField(default=False, verbose_name='Es admin')),  # noqa: E501
                ('is_superuser', models.BooleanField(default=False, verbose_name='Es super usuario')),  # noqa: E501
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),  # noqa: E501
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),  # noqa: E501
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),  # noqa: E501
            ],
            options={
                'verbose_name': 'Usuario',
            },
        ),
    ]
