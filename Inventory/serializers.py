from rest_framework import serializers
from .models import *

class Product_Serializer(serializers.Serializer):
    class Meta:
        model = Products
        feilds ='__all__'
        