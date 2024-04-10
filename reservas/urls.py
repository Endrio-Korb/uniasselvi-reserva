from django.urls import path


from .views import ReservarLabs, CancelarForm
from .views import editar_form, registrarReservarLaboratorio, modules, editar, editar_modules

app_name = "reservas"

urlpatterns = [
    path('reservas/', ReservarLabs.as_view(), name='reserva_form'),    
    path('(^?P<pk>[0-9]+)/cancelar', CancelarForm.as_view(), name='cancelar_form'),

    
    path('', registrarReservarLaboratorio, name='registrar_reserva'),
    path('modules/', modules, name='modules'),
    path('editar_modules/', editar_modules, name='editar_modules'),

    #path('<int:pk>/editar', Editar.as_view(), name='editar'),
    path('(^?P<pk>[0-9]+)/editar_form', editar_form, name='editar_form'),
    path('(^?P<pk>[0-9]+)/editar', editar, name='editar'),
]

