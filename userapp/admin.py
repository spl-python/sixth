from django.contrib import admin

from userapp import models

admin.site.register(models.User)
admin.site.register(models.Employee)
