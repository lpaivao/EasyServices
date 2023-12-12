from django.urls import path
from .views import PrestadorListCreateView, PrestadorRetrieveUpdateDestroyView, PrestadorObtainTokenView, PrestadorLogoutView

urlpatterns = [
    path('prestadores/', PrestadorListCreateView.as_view(), name='prestador-list-create'),
    path('prestadores/<int:pk>/', PrestadorRetrieveUpdateDestroyView.as_view(), name='prestador-retrieve-update-destroy'),
    path('prestadores/token/', PrestadorObtainTokenView.as_view(), name='prestador-obtain-token'),
    path('prestadores/logout/', PrestadorLogoutView.as_view(), name='prestador-logout')
]