from django.urls import path, re_path


from .views import ReservarLabs
from .views import editar_form, registrarReservarLaboratorio, modules, editar, editar_modules, cancelar_form, cancelar_reserva

app_name = "reservas"

urlpatterns = [
    path('reservas/', ReservarLabs.as_view(), name='reserva_form'),    
    re_path('(?P<id>[0-9]+)/cancelar', cancelar_form, name='cancelar_form'),
    re_path('(?P<id>[0-9])/cancelar_reserva', cancelar_reserva, name="cancelar_reserva"),

    
    path('', registrarReservarLaboratorio, name='registrar_reserva'),
    path('modules/', modules, name='modules'),
    path('editar_modules/', editar_modules, name='editar_modules'),

    #path('<int:pk>/editar', Editar.as_view(), name='editar'),
    re_path('^(?P<id>[0-9]{1})/editar_form', editar_form, name='editar_form'),
    re_path('(?P<id>[0-9]{1})/editar', editar, name='editar'),
]

