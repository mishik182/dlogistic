from rest_framework import generics

from models.models import (
    Account,
)

from account.serializers import (
    AccountSerializer,
)


class AccountListCreateView(generics.ListAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# class AccountTypeListCreateView(generics.ListCreateAPIView):
#     serializer_class = AccountTypeEditSerializer
#     queryset = Accounttype.objects.all()
#     permission_classes = [IsOwnerOrReadOnly]
#     permission_classes = [IsAuthenticated, IsAdminUser]
#     permission_classes = [AllowAny]
#     user = authenticate(username='noom', password='blink182')
#
#     def perform_create(self, serializer):
#         serializer.save(createbyid=self.request.user)
#         serializer.save(createbyid=str(self.user.first_name) + ' ' + str(self.user.last_name))
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#
#     queryset = Accounttype.objects.all()
#     serializer_class = AccountTypeEditSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
