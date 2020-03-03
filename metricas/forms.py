from django import forms
from django.views.generic.list import ListView

from .models import Metrica


class MetricForm(forms.Form):
    METRICAS_CHOICES = [
    ('CPU', 'CPU'),
    ('Memória', 'Memória'),
    ('Disco', 'Disco'),
    ]

    GRANULARIDADE_CHOICES = [
    (1, 'Hora'),
    (2, 'Dia'),
    (3, 'Semana'),
    (3, 'Mês'),
    ]
    
    nome = forms.CharField(
        max_length=200,
        widget=forms.Select(choices=METRICAS_CHOICES),
    )
    granularidade = forms.MultipleChoiceField(widget=forms.SelectMultiple,
                                         choices=GRANULARIDADE_CHOICES, required=False)


    def get_metricas(self, nome):
        return Metrica.objects.filter(nome=nome)


class MetricListView(ListView):

    model = Metrica
    paginate_by = 100  # if pagination is desired