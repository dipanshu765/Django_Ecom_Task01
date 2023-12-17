from rest_framework.serializers import ModelSerializer
from pages.models import Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'category', 'brand', 'image', 'price', 'quantity', 'description']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.name

        return token
