from django import forms
from datetime import date
from proyecto.models import Proyecto
from .models import PagoPaypal

class PayPalForm(forms.ModelForm):
	class Meta:
		model = PagoPaypal
		fields = (
			'Proyecto',
			'payment_id',
			'payer_id',
			'payer_email',
			'donate',
		)
