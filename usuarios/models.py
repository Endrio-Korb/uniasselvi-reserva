from django.db import models
from uuid import uuid4
# Create your models here.

class PreRegistro(models.Model):

    email = models.EmailField("E-mail", max_length=200)
    uuid = models.UUIDField(default=uuid4)
    data_hora = models.DateTimeField(auto_now_add=True)
    valido = models.BooleanField(default=True)

    class Meta:
        db_table = "tb_pre_registro"