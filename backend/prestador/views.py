from rest_framework import generics
from .models import Prestador
from .serializers import PrestadorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

class PrestadorListCreateView(generics.ListCreateAPIView):
    queryset = Prestador.objects.all()
    serializer_class = PrestadorSerializer
    #permission_classes = [IsAuthenticated]
    

class PrestadorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prestador.objects.all()
    serializer_class = PrestadorSerializer
    lookup_field = 'id'
    #permission_classes = [IsAuthenticated]

class PrestadorObtainTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = Prestador.objects.get(email=email, password=password)
        except Prestador.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({'access_token': access_token, 'refresh_token': refresh_token},status=status.HTTP_200_OK)
    
class PrestadorLogoutView(APIView):
    #permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if not refresh_token:
            return Response({"error": "Refresh token is required."}, status=400)

        try:
            #RefreshToken(refresh_token).blacklist()
            return Response({"message": "Logout successful."})
        except Exception as e:
            return Response({"error": str(e)}, status=500)