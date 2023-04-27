from django.contrib import admin

from . import models

admin.site.register(models.SuperAdmin)
admin.site.register(models.States)
admin.site.register(models.Districts)
admin.site.register(models.Categories)
admin.site.register(models.SubCategories)
admin.site.register(models.Mandal)
