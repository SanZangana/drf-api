from rest_framework import generics
from apis.permissions import IsOwnerOrReadOnly
from .models import Account
from .serializers import AccountSerializer


class AccountList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer