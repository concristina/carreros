from django.contrib import admin
from .models import Problema
# Register your models here.


class ProblemaAdmin(admin.ModelAdmin):
    list_display = ('problema', 'mesa', 'descripcion', 'reportado_por', 'estado')
    list_filter = ('problema', 'estado')
    search_fields = (
        'mesa__numero',
    )


admin.site.register(Problema, ProblemaAdmin)