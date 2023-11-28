# apps/plano/forms.py
from django import forms
from .models import TblCidade

class SelectCityForm(forms.Form):
    cdd_id = forms.ModelChoiceField(
        queryset=TblCidade.objects.all(),
        empty_label="Escolha a cidade",
        label="Cidade",
        widget=forms.Select(attrs={'class': 'form-select mb-3'})
    )
