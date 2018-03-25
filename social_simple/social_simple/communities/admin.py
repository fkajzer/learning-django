from django.contrib import admin
from . import models
# Register your models here.


class GroupMember(admin.TabularInline):
    model = models.Member


admin.site.register(models.Community)
