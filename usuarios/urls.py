from django.urls import path

from .views import login_user, login_form, logout_user, pre_registro, reenviar_pre_registro
from .views import processar_login, registrar

app_name = 'usuarios'

urlpatterns = [
    path('logout/', logout_user, name='logout'),
    path("login/", login_form, name="login_form"),
    path('login_user/', login_user, name='login_user'),
    path("pre/", pre_registro, name="pre_registro"),
    path("pre/<uuid>/reenviar", reenviar_pre_registro, name="reenviar_pre_registro"),
    path("confirmacao/", registrar, name="registrar"),
    path("processar-login/", processar_login, name="processar_login"),
]
