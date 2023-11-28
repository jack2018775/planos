from django.shortcuts import render, get_object_or_404
from .models import TblCidade, TblPlano, TblAcordos

# Create your views here.
def planos_by_city(request, cdd_id):
    city = get_object_or_404(TblCidade, pk=cdd_id)
    planos = TblPlano.objects.filter(tblciddplan__cdd=city)
    
    for plano in planos:
        plano.itens = plano.tblplaniten_set.all()
        plano.acordos = TblAcordos.objects.filter(acor_plan=plano)
        ...
    
    return render(request, 'planos/planos_by_city.html', {'city': city, 'planos': planos})