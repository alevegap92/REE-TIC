from django import forms

from proyecto.models import proyecto


class ProyectoForm(forms.ModelForm):
	class Meta:
		model = proyecto

		fields = [
			'titulo',
			'logo',
			'descripcion_general',
			'descripcion_detallada',
			'definicion_problema',
			'definicion_solucion',
			'video',
		]
		labels = {
			'titulo': 'Nombre del Proyecto',
			'descripcion_general': 'Descripcion General',
			'descripcion_detallada': 'Visión general del negocio',
			'definicion_problema':'Definicion del Problema',
			'definicion_solucion': 'Solucion propuesta',
		}
		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion_detallada': forms.Textarea(attrs={'class':'form-control'}),
			'descripcion_general': forms.Textarea(attrs={'class':'form-control'}),
			'definicion_problema': forms.Textarea(attrs={'class':'form-control'}),
			'definicion_solucion': forms.Textarea(attrs={'class':'form-control'}),
		}
