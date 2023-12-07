from django.urls import path
from .views import ClienteListCreateView, ClienteRetrieveUpdateDestroyView

urlpatterns = [
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('clientes/<int:id>/', ClienteRetrieveUpdateDestroyView.as_view(), name='reader-retrieve-update-destroy'),
]