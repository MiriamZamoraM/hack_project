from django.contrib import admin

from .models import Corepath
from .models import CoreUser

# Register your models here.
admin.site.register(Corepath)
admin.site.register(CoreUser)
