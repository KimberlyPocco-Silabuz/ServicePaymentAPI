from rest_framework.serializers import ModelSerializer
from servicespayment.models import Services, Payment_user,Expired_payments


class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


class Payment_userSerializer(ModelSerializer):
    class Meta:
        model = Payment_user
        fields = "__all__"

class Expired_paymentSerializer(ModelSerializer):
    class Meta:
        model = Expired_payments
        fields = "__all__"