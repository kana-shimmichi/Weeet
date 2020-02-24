from django.urls import path
from . import views


app_name = 'home'


urlpatterns = [
    ##TOP
    path('', views.Top.as_view(), name='top'),



    path('menu/', views.Menu.as_view(), name='top'),

    path('about/', views.About.as_view(), name='about'),
    path('instructions/', views.About.as_view(), name='instructions'),
    path('question/', views.Question.as_view(), name='question'),
    ##COMPLETE
    path('choice_role/', views.RoleChoice.as_view(), name='choice_role'),
    path('add_role/', views.addRole, name='add_role'),
    path('add_profile/', views.addProfile, name='add_profile'),
    path('change_profile/', views.change_profile, name="change_profile"),

    path('menu/', views.menu, name='menu'),


    path('diagnosis/', views.Diagnosis.as_view(), name='diagnosis'),


    path('order_submit/', views.OrderSubmit.as_view(), name='order_submit'),
    path('orders_list/', views.OrdersList.as_view(), name='orders_list'),


    path('contact/<int:id>', views.Contacts.as_view(), name='contacts'),
    path('add_like/<int:id>', views.addLike, name='add_like'),


    path('request/', views.Request.as_view(), name='request'),

    path('makers/', views.Makers.as_view(), name='makers'),
    path('makers_edit/', views.MakersEdit.as_view(), name='makers_edit'),

    path('messages/', views.Message.as_view(), name='top'),
    path('message_detail/', views.MessageDetail.as_view(), name='top'),
    path('order/', views.Order.as_view(), name='top'),
    path('order_reply/', views.OrderReply.as_view(), name='top'),
    path('order_pay/', views.OrderPay.as_view(), name='top'),
]
