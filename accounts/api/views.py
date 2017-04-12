from rest_framework.generics import CreateAPIView, ListAPIView
from ..models import Account
from .serializers import CreateAccountSerializer, ListAccountSerializer
from rest_framework.permissions import IsAuthenticated

class CreateAccountAPIView(CreateAPIView):
	queryset = Account.objects.all()
	serializer_class = CreateAccountSerializer

class ListAccountAPIView(ListAPIView):
	queryset = Account.objects.all()
	serializer_class = ListAccountSerializer
	permission_classes = (IsAuthenticated,)