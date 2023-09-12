from django import forms
from .models import Wisata
class WisataChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj): return obj.nama


class KomentarForm(forms.Form):
    wisata = WisataChoiceField(queryset=Wisata.objects.all() )
    kalimat = forms.CharField(label = 'Kalimat',widget = forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))

    def __init__(self, *args, **kwargs):
        super(KomentarForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if hasattr(visible.field.widget, 'input_type'):
                if visible.field.widget.input_type in ['radio', 'checkbox']:
                    visible.field.widget.attrs['class'] = 'form-check-input'
                else:
                    visible.field.widget.attrs['class'] = 'form-control'
