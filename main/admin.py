from django.contrib import admin
from . models import Data

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'title',
        'description'
    )
admin.site.register(Data, DataAdmin)