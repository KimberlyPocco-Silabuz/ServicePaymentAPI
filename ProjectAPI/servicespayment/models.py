from django.db import models
from django.contrib.auth.models import User

'''
modelo servicios trabaja con el user por default de django
'''
class Services(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField()
    logo = models.CharField(max_length=100)
    
    class Meta:
        db_table = "services"

'''
modelo payment 
'''
class Payment_user(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    service_id = models.ForeignKey(Services,on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    paymentDate = models.DateTimeField()
    expirationDate = models.DateTimeField()
    
    class Meta:
        db_table = "payment_user"

'''
modelo expired  payments
'''
class Expired_payments(models.Model):
    payment_user_id = models.ForeignKey(Payment_user,on_delete=models.CASCADE)
    penalty_fee_amount= models.IntegerField()

    class Meta:
        db_table = "expired_payments"