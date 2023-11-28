# apps/plano/views.py
from django.shortcuts import render, redirect
from apps.planos.models import TblCidade
from apps.planos.forms import SelectCityForm
from django.urls import reverse

def home(request):
    if request.method == 'POST':
        form = SelectCityForm(request.POST)
        if form.is_valid():
            cdd_id = form.cleaned_data['cdd_id'].cdd_id
            return redirect(reverse('planos_by_city', args=[cdd_id]))
    else:
        form = SelectCityForm()

    cities = TblCidade.objects.all()
    return render(request, 'core/home.html', {'form': form, 'cities': cities})
