from django.urls import path
from . import views


app_name = 'account'


urlpatterns = [
    path('', views.login_page, name='login'),
    path('registration_user', views.registration_page, name='registration'),
    path('logout_user', views.logout_user, name='logout'),

]
