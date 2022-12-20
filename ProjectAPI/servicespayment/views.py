from rest_framework.viewsets import ModelViewSet,ViewSet, ReadOnlyModelViewSet
from .models import Services, Payment_user, Expired_payments
from .serializers import ServicesSerializer, Payment_userSerializer, Expired_paymentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle

#CRUD SERVICCES VIEWSET
class ServicesViewSet(ModelViewSet):
    
    serializer_class = ServicesSerializer

    def get_queryset(self):
        permission_classes=[IsAuthenticated] 
        return Services.objects.all()
   
    def get_object(self, queryset=None, **kwargs):
        item_services= self.kwargs.get('pk')
        return get_object_or_404(Services, id=item_services)
       

       
#CRUD PAYMENT USER VIEWSET
class Payment_userViewSet(ModelViewSet):
  
    queryset = Payment_user.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        return Payment_userSerializer


    def list(self, request, *args):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args):
        if isinstance(request.data, list):
            serializer = Payment_userSerializer(data=request.data, many = True)
        else:
            serializer = Payment_userSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = Payment_userSerializer(todo)
        return Response(serializer.data)

    def update(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = Payment_userSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def destroy(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#CRUD EXPIRED PAYMENTS VIEWSET
class Expired_paymentsViewSet(ModelViewSet):
    serializer_class = Expired_paymentSerializer
    def get_queryset(self):
        return Expired_payments.objects.all()

    def get_object(self, queryset=None, **kwargs):
        item_expiredpay= self.kwargs.get('pk')
        return get_object_or_404(Expired_payments, id=item_expiredpay)
     