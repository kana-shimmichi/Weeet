from django.urls import path
from . import views


app_name = 'trade'


urlpatterns = [
    path('menu/', views.Request.as_view(), name='request'),
    path('consent/', views.Consent.as_view(), name='consent'),
    path('delivery/', views.Delivery.as_view(), name='delivery'),
    path('credit/', views.Credit.as_view(), name='credit'),
    path('decline/', views.Decline.as_view(), name='decline'),
]