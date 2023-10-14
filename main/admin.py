from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.UserInfo)
admin.site.register(models.UserMood)
admin.site.register(models.Memories)
admin.site.register(models.Medications)
admin.site.register(models.MedicationsRecord)