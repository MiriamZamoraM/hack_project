from django.db import models
from users.models import User

# Create your models here.


class Corepath(models.Model):
    name = models.CharField(max_length=50, verbose_name='Tronco Común')
    description = models.TextField(verbose_name='Descripción')
    status_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'Core'
        verbose_name = 'Core'


class SubCorePath(models.Model):
    name = models.CharField(max_length=50, verbose_name='Sub Tronco')
    description = models.TextField(verbose_name='Descripción')
    core = models.ForeignKey(Corepath, on_delete=models.CASCADE)
    status_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'SubCorePath'
        verbose_name = 'SubPaths'


class CoreUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sub_core = models.ForeignKey(SubCorePath, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    url_repo = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'CoreUser'
        verbose_name = 'CoreUser'
