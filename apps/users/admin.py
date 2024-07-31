from django.contrib import admin  # noqa: F401

from .models import User


# Register your models here.
admin.site.register(User)
