from django import forms
from .models import Tienda, Ciudad, Region

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ciudad'].queryset = Ciudad.objects.none()

        if 'region' in self.data:
            try:
                idregion = int(self.data.get('region'))
                self.fields['ciudad'].queryset = Ciudad.objects.filter(idRegion=idregion).order_by('descripcion')
            except (ValueError, TypeError):
                pass