from django.urls import path
from . import views


app_name = 'my_page'


urlpatterns = [
    path('my_menu/', views.menu, name='my_menu'),

    path('order_submit/<int:order_id>', views.submit, name='submit'),


    path('profile/', views.Profile.as_view(), name='profile'),

    path('register_info/', views.Register_Info.as_view(), name='register_info'),
    path('orderer_info/', views.Orderer_Info.as_view(), name='orderer_info'),
    path('contractor_info/', views.Contractor_Info.as_view(), name='contractor_info'),

    path('message/', views.message, name='message'),
    path('message/<int:customer_id>/', views.message, name='message_detail'),

    path('order_decide/<int:order_id>/<int:customer_id>/', views.order_decide, name='order_decide'),

    path('pay/<int:order_id>', views.pay, name='pay'),
    path('pay_credit/<int:order_id>',views.pay_credit,name='pay_credit'),

    path('cancel/<int:order_id>',views.cancel,name='cancel'),
    path('order_fin/<int:order_id>',views.order_fin,name='order_fin'),
    path('complete/<int:order_id>', views.complete, name="complete"),


    path('favorite_list/', views.Favorite_List.as_view(), name='favorite_list'),
    path('request_job/', views.Request_Job.as_view(), name='request_job'),
    path('consent_list/', views.Consent_list.as_view(), name='consent_list'),
    path('trade_list/', views.Trade_list.as_view(), name='trade_list'),
    path('complate_list/', views.Complate_list.as_view(), name='complate_list'),



    path('comfirm/', views.Comfirm.as_view(), name='comfirm'),
    path('change/', views.Change.as_view(), name='change'),
    path('approval/', views.Approval.as_view(), name='approval'),
    path('cancel/', views.Cancel.as_view(), name='cancel'),
    path('complate/', views.Complate.as_view(), name='complate'),

]