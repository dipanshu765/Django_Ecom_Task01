from rest_framework.decorators import api_view
from rest_framework.response import Response
from pages.models import Product
from .serializers import ProductSerializer
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/products',
        'GET /api/products/:product_id'
    ]
    return Response(routes)


@api_view(['GET'])
def getProducts(request):

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, product_id):

    product = Product.objects.get(id=product_id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
