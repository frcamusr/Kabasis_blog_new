from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class PlanPago(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    category_id = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    currency_id = models.CharField(max_length=50)
    alumnos = models.IntegerField()

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category_id": self.category_id,
            "quantity": self.quantity,
            "unit_price": self.unit_price,
            "currency_id": self.currency_id
        }
    

 
class RegistroTransaccion(models.Model):
    payment_id = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    merchant_order_id = models.CharField(max_length=255)
    fecha_transaccion = models.DateField()
    hora_transaccion = models.TimeField()
    id_plan = models.ForeignKey(PlanPago, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.payment_id} - {self.status} - {self.fecha_transaccion} {self.hora_transaccion}"


from django.db import models

class Zona(models.Model):
    comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.comuna} - {self.region}"


class datosComprador(models.Model):
    id_plan = models.ForeignKey(PlanPago, on_delete=models.CASCADE)
    tipoDocumento = models.CharField(max_length=255)
    rutEmpresa = models.CharField(max_length=255)
    razonSocial = models.CharField(max_length=255)
    giro = models.CharField(max_length=255)
    DireccionTributaria = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    nombreComprador = models.CharField(max_length=255)
    rutComprador = models.CharField(max_length=255)
    correoComprador = models.CharField(max_length=255)
    numeroContacto = models.CharField(max_length=255)
    estadoPago = models.BooleanField(default = False)


    