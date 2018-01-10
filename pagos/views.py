from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views.generic import RedirectView, TemplateView
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponseBadRequest
from .models import PagoPaypal


import paypalrestsdk
#from .models import *
from proyecto.models import Proyecto
class PaypalView(RedirectView):

    permanent = False

    def _generar_lista_items(self, Proyecto):
        """ """
        items = []
        items.append({
            "name":     str(Proyecto),
            "sku":      str(Proyecto.id),
            "price":    ('%.2f' % Proyecto.donate),
            "currency": 'USD',
            "quantity": 1,
        })
        return items

    def _generar_peticion_pago_paypal(self, Proyecto):
        """Crea el diccionario para genrar el pago paypal de proyecto"""
        peticion_pago = {
            "intent": "sale",
            "payer": {"payment_method": "paypal"},
            "redirect_urls": {
                "return_url": settings.SITE_URL+reverse('aceptar-pago-paypal'),
                "cancel_url": settings.SITE_URL},

            # Transaction -
            "transactions": [ {
                # ItemList
                "item_list":{
                    "items": self._generar_lista_items(Proyecto)},

                # Amount
                "amount": {
                    "total": ('%.2f' % Proyecto.donate),
                    "currency": 'USD'},

                #Description
                "description": str(Proyecto),}
            ]}

        return peticion_pago

    def _generar_pago_paypal(self, Proyecto):
        """Genera un pago de paypal para proyecto"""
        paypalrestsdk.configure({
            "mode":         settings.PAYPAL_MODE,
            "client_id":    settings.PAYPAL_CLIENT_ID,
            "client_secret":settings.PAYPAL_CLIENT_SECRET,})

        pago_paypal = paypalrestsdk.Payment(self._generar_peticion_pago_paypal(Proyecto))

        if pago_paypal.create():
            for link in pago_paypal.links:
                if link.method == "REDIRECT":
                    url_pago = link.href
        else:
            raise Exception(pago.error)

        return url_pago, pago_paypal

    def get_redirect_url(self, *args, **kwargs):
        """Extrae el proyecto que el usuario quiere comprar, genera un pago de
        paypal por el donate del proyecto, y devuelve la direccion de pago que
        paypal generó"""
        proyecto = get_object_or_404(Proyecto, pk=int(kwargs['proyecto_pk']))
        url_pago, pago_paypal = self._generar_pago_paypal(proyecto)

        # Se añade el identificador del pago a la sesion para que PaypalExecuteView
        # pueda identificar al ususuario posteriorment
        self.request.session['payment_id'] = pago_paypal.id

        # Por ultimo salvar la informacion del pago para poder determinar que
        # proyecto le corresponde, al terminar la transaccion.
        PagoPaypal.objects.crear_pago(pago_paypal.id, proyecto)

        return url_pago

class PaypalExecuteView(TemplateView):

    template_name = 'paypal/paypal_exito.html'

    def _enviar_ebook_email(self, registro_pago):
        """Enviar Email con el proyecto al cliente """
        #TODO: adjuntar los archivos del modelo proyecto
        Proyecto = registro_pago.Proyecto
        mensaje = "Gracias a tu donacion está mas cerca de cumplir su sueño el grupo de %s" % Proyecto.titulo
        send_mail('Red de Emprendimiento Escolar [REE][CHL]', mensaje,
            from_email = settings.DEFAULT_FROM_EMAIL,
            recipient_list=[registro_pago.payer_email,])

    def _aceptar_pago_paypal(self, payment_id, payer_id):
        """Aceptar el pago del cliente, actualiza el registro con los datos
        del cliente proporcionados por paypal"""
        registro_pago = get_object_or_404(PagoPaypal, payment_id=payment_id)
        pago_paypal = paypalrestsdk.Payment.find(payment_id)
        if pago_paypal.execute({'payer_id': payer_id}):
            registro_pago.pagado = True
            registro_pago.payer_id = payer_id
            registro_pago.payer_email = pago_paypal.payer['payer_info']['email']
            registro_pago.save()
        else:
            raise HttpResponseBadRequest

        return registro_pago

    def get(self, request, *args, **kwargs):
        """Extraer identificacion de paypal del cliente, la id del pago,
        aceptar el pago, y enviar el email."""
        context = self.get_context_data(**kwargs)
        try:
            payer_id = request.GET['PayerID']
            payment_id = request.session['payment_id']
        except Exception:
            raise HttpResponseBadRequest

        registro_pago = self._aceptar_pago_paypal(payment_id, payer_id)
        self._enviar_ebook_email(registro_pago)

        return self.render_to_response(context)


#--------Presentar datos en las Vista Template-----------------#
#Nada funciona son solo ideas
def intWithCommas(x):
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)

def get_context():
    total = PagoPaypal.objects.all().aggregate(Sum('donate'))['donate__sum']
    pct = ((100 * float(total) / float(Proyecto.donate)) if total else 0)
    #total_donadores = PagoPaypal.objects.filter(payer_email__pk = self.id).count()
    c = Context({
        'goal': intWithCommas(Proyecto.donate),
        'Donadores': PagoPaypal.objects.count(),
        'pct': pct,
        'pct_disp': (int(pct) if total else 0),
        'total': (intWithCommas(int(total)) if total else '0'),
        })
    return c
   # return render(request, 'proyecto/proyecto_list.html', c)

def get_total_pagos():
    total = PagoPaypal.objects.values('Proyecto__titulo').annotate(Sum('donate'))
    donadores = PagoPaypal.objects.values('Proyecto__titulo').count()
    return total
