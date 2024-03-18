from rest_framework import generics, status
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer, UserRegisterSerializer


class IsOwnerOrReadOnly(BasePermission):
    """ Является ли пользователь владельцем объекта """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.pk == request.user.pk


class UsersListView(generics.ListAPIView):
    """ Список пользователей """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UsersRetrieveAPIView(generics.RetrieveAPIView):
    """ Детали пользователя """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UsersCreateView(generics.CreateAPIView):
    """ Создание нового пользователя """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UsersUpdateView(generics.UpdateAPIView):
    """ Обновления информации по пользователю (разрешено только владельцу объекта) """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UsersDeleteView(generics.DestroyAPIView):
    """ Удаление пользователя (разрешено только владельцу объекта) """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]


class UsersRegistrationView(generics.CreateAPIView):
    """ Регистрация нового пользователя """
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)
