from rest_framework.viewsets import ModelViewSet,ViewSet, ReadOnlyModelViewSet
from .models import Services, Payment_user, Expired_payments
from .serializers import ServicesSerializer, Payment_userSerializer, Expired_paymentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import filters
from django.shortcuts import get_object_or_404

'''
CRUD de modelo servicios
'''
class ServicesViewSet(ModelViewSet):
    
    serializer_class = ServicesSerializer
    
    #trae todos los metodos crud por id 
    def get_object(self, queryset=None, **kwargs):
        item_services= self.kwargs.get('pk')
       
        return get_object_or_404(Services, id=item_services)
        #trae todos los crud por id llama al item servicio 
        #Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
        #http://127.0.0.1:8000/services-payment/services/id
        #http://127.0.0.1:8000/services-payment/services/1
    
    #definir el queryset custom o personalizado
    def get_queryset(self):
        permission_classes=[AllowAny] 
        return Services.objects.all()
        #hace el get y post (create y list)
        #Allow: GET, POST, HEAD, OPTIONS
        ##http://127.0.0.1:8000/services-payment/services/
   

'''
CRUD de modelo payments_user
'''
class Payment_userViewSet(ModelViewSet):
    serializer_class = Payment_userSerializer

     #trae todos los metodos crud por id 
    def get_object(self, queryset=None, **kwargs):
        item_payment= self.kwargs.get('pk')
        return get_object_or_404(Payment_user, id=item_payment)
        #crea un registro primero para poner el 1 que es el primer id 
        #http://127.0.0.1:8000/services-payment/payment-user/id
        #http://127.0.0.1:8000/services-payment/payment-user/1
    
    #definir el queryset custom o personalizado
    def get_queryset(self):
        return Payment_user.objects.all()
        #hace el get y post (create y list)
        #Allow: GET, POST, HEAD, OPTIONS
        #http://127.0.0.1:8000/services-payment/payment-user/

'''
CRUD de modelo servicios
'''
class Expired_paymentsViewSet(ModelViewSet):
    serializer_class = Expired_paymentSerializer
    
     #trae todos los metodos crud por id 
    def get_object(self, queryset=None, **kwargs):
        item_expiredpay= self.kwargs.get('pk')
        return get_object_or_404(Expired_payments, id=item_expiredpay)
        #http://127.0.0.1:8000/services-payment/expired-payments/1
    
    #definir el queryset custom o personalizado
    def get_queryset(self):
        return Expired_payments.objects.all()
        #http://127.0.0.1:8000/services-payment/expired-payments/