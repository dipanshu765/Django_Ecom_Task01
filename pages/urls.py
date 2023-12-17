from django.urls import path
from . import views


app_name = 'pages'


urlpatterns = [
    path('', views.index, name='index'),
    path('product/<str:product_id>/', views.product_page, name='product_page'),
    path('delete_product/<str:product_id>/', views.delete_product, name='delete_product'),
    path('add_product', views.add_product, name='add_product'),
    path('update_room/<str:product_id>/', views.updateProduct, name='update_product')
]
