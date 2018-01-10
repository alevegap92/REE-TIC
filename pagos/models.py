from django.db import models
from decimal import Decimal
from proyecto.models import Proyecto

class PagoPaypalManager(models.Manager):
    def crear_pago(self, payment_id, Proyecto):
        pago=self.create(Proyecto=Proyecto,
            payment_id=payment_id,  
            donate=Proyecto.donate)
        return pago

class PagoPaypal(models.Model):
    # Foreign Key hacia el Proyecto de este pago
    Proyecto = models.ForeignKey(Proyecto)

    # Identificador de paypal para este pago
    payment_id = models.CharField(max_length=64, db_index=True)

    # Id unico asignado por paypal a cada usuario no cambia aunque
    # la dirección de email lo haga.
    payer_id = models.CharField(max_length=128, blank=True, db_index=True)

    # Dirección de email del cliente proporcionada por paypal.
    payer_email = models.EmailField(blank=True)

    # Guardamos una copia del donate de Proyecto, porque puede variar en el tiempo
    donate = models.DecimalField(max_digits=8, decimal_places=2,
                default = Decimal('0.00'))

    pagado = models.BooleanField(default=False)

    objects = PagoPaypalManager()
