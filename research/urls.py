from django.urls import path
from . import views


app_name = 'research'


urlpatterns = [
    path('contractor_form', views.Contractor_form.as_view(), name='contractor_form'),
    path('contractor_result.html/', views.Contractor_result.as_view(), name='contractor_result'),
    path('orderer_form.html/', views.Orderer_form.as_view(), name='orderer_form'),
    path('orderer_result.html/', views.Orderer_result.as_view(), name='orderer_result'),
]