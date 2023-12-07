from django.urls import path
from .views import PrestadorListCreateView, PrestadorRetrieveUpdateDestroyView

urlpatterns = [
    path('prestadores/', PrestadorListCreateView.as_view(), name='prestador-list-create'),
    path('prestadores/<int:id>/', PrestadorRetrieveUpdateDestroyView.as_view(), name='prestador-retrieve-update-destroy'),
]