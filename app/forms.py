from django import forms
from .models import Factura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = [
            'idFactura',
            'idUsuario',
            'idProducto',
            'cantidad',
            #'dateTime',
        ]

        labels = {
            'idFactura':'IdFactura',
            'idUsuario':'IdUsuario',
            'idProducto':'IdProducto',
            'cantidad':'Cantidad',
            #'dateTime' : 'Date Time',
        }