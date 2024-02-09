from django.contrib.auth.models import User
from .models import Orders, Categories
from .serializers import OrderSerializers, UserSerializers, CategoriesSerializers
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly


# Информация о пользователях
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


# Заявки
class OrdersList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


# Категории
class CategoriesList(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers
