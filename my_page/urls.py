from django.urls import path
from . import views


app_name = 'my_page'


urlpatterns = [
    path("order/",views.Order.as_view(),name='order'),
    path('my_menu/', views.Menu.as_view(), name='my_menu'),
    path('favorite/', views.Favorite.as_view(), name='favorite'),
    path('message/', views.Message.as_view(), name='message'),
    path('trade_list/', views.Tradelist.as_view(), name='trade_list'),
]