from django.contrib import admin
from models import *

class DatasetAdmin(admin.ModelAdmin):
	list_display = ('name',)
	ordering = ('name',)

class DatasetItemAdmin(admin.ModelAdmin):
	list_display = ('dataset', 'content', 'time', 'lat', 'long',)
	ordering = ('dataset', '-time')

admin.site.register(Dataset, DatasetAdmin)
admin.site.register(DatasetItem, DatasetItemAdmin)

