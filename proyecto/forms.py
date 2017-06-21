from django import forms
from datetime import date
from .models import Proyecto, Picture


class ProyectoForm(forms.ModelForm):
	class Meta:
		model = Proyecto

		fields = [
			'titulo',
			'logo',
			'descripcion_general',
			'descripcion_detallada',
			'definicion_problema',
			'definicion_solucion',
			'video',
			'donate',
		]
		labels = {
			'titulo': 'Nombre del Proyecto',
			#'logo': 'Cargar logo del proyecto',
			'descripcion_general': 'Descripcion General',
			'descripcion_detallada': 'Visión general del negocio',
			'definicion_problema':'Definicion del Problema',
			'definicion_solucion': 'Solucion propuesta',
			'donate' :'Monto a recaudar',
		}
		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion_detallada': forms.Textarea(attrs={'class':'form-control'}),
			'descripcion_general': forms.Textarea(attrs={'class':'form-control'}),
			'definicion_problema': forms.Textarea(attrs={'class':'form-control'}),
			'definicion_solucion': forms.Textarea(attrs={'class':'form-control'}),
			'video': forms.TextInput(attrs={'class':'form-control'}),
		}
		exclude = ('usuario',)

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        #fields = ['picture',]
        exclude = ('proyecto_picture',)
