from django.contrib import admin
from .models import kegiatan

@admin.register(kegiatan)
class ModelKegiatan(admin.ModelAdmin):
    list_filter = ('name','description')
    list_display = ('name','description')
