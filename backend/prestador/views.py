from rest_framework import generics
from .models import Prestador
from .serializers import PrestadorSerializer

class PrestadorListCreateView(generics.ListCreateAPIView):
    queryset = Prestador.objects.all()
    serializer_class = PrestadorSerializer
    

class PrestadorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestador.objects.all()
    serializer_class = PrestadorSerializer
    lookup_field = 'id'