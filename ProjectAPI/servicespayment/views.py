from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Services, Payment_user, Expired_payments
from .serializers import ServicesSerializer, Payment_userSerializer, Expired_paymentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import filters

'''
CRUD de modelo servicios
'''
class ServicesViewSet(ModelViewSet):
    queryset = Services.objects.all()
     
    def get_serializer_class(self):
        return ServicesSerializer

    def list(self, request):
        pass
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


'''
CRUD de modelo payments_user
'''
class Payment_userViewSet(ModelViewSet):
    queryset = Payment_user.objects.all()

    def get_serializer_class(self):
        return Payment_userSerializer

    def list(self, request):
        pass
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


'''
CRUD de modelo servicios
'''
class Expired_paymentsViewSet(ModelViewSet):
    queryset = Expired_payments.objects.all()

    def get_serializer_class(self):
        return Expired_paymentSerializer

    def list(self, request):
        pass
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)