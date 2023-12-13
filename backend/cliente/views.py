from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.authtoken.views import ObtainAuthToken, Token
from rest_framework.permissions import AllowAny, IsAuthenticated

class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = [IsAuthenticated]
    
class ClienteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = [IsAuthenticated]

class ClienteObtainTokenView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key, 'user_id': user.pk, 'email': user.email})

class ClienteLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth.delete()
        return Response({"message": "Logout successful."})