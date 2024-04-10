from django.contrib import admin

# Register your models here.
from .models import Laboratorios, ReservasLaboratorios, Blocos, Periodos
admin.site.register(Laboratorios)
admin.site.register(ReservasLaboratorios)
admin.site.register(Blocos)
admin.site.register(Periodos)