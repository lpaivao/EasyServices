from django.urls import path
from .views import ClienteListCreateView, ClienteRetrieveUpdateDestroyView, ClienteObtainTokenView, ClienteLogoutView

urlpatterns = [
    path('clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroyView.as_view(), name='reader-retrieve-update-destroy'),
    path('clientes/token/', ClienteObtainTokenView.as_view(), name='cliente-obtain-token'),
    path('clientes/logout/', ClienteLogoutView.as_view(), name='cliente-logout')
]