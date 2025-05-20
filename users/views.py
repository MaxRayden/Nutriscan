from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .serializers import UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    # [IsAuthenticated] depois mudar

    def get_queryset(self):
        # Apenas o próprio usuário vê seus dados
        # return User.objects.filter(id=self.request.user.id)
        return User.objects.all()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]