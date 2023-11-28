# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:cdd_id>/', views.planos_by_city, name='planos_by_city'),
    # ... outras URLs ...
]