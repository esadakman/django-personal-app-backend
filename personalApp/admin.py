from django.contrib import admin

# Register your models here.
from .models import Department, Personal


admin.site.register(Department)
admin.site.register(Personal)