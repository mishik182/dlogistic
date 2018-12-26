from rest_framework import generics
from rest_framework.permissions import (
    AllowAny, IsAuthenticated,
    IsAdminUser, IsAuthenticatedOrReadOnly
)
from models.models import (
    AuthUser, Accounttype,
)
from .serializers import (
    AccountTypeSerializer,
)


class AccountTypeListCreateView(generics.ListCreateAPIView):
    serializer_class = AccountTypeSerializer
    queryset = Accounttype.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = AuthUser.objects.get(username=self.request.user)
        serializer.save(createbyid=user.id)


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AccountTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Accounttype.objects.all()
    serializer_class = AccountTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        user = AuthUser.objects.get(username=self.request.user)
        serializer.save(modifiedbyid=user.id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
