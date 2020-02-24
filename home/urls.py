from django.urls import path
from . import views


app_name = 'home'




urlpatterns = [
    ##COMPLETE
    path('', views.Top.as_view(), name='top'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('question/', views.Question.as_view(), name='question'),
    path('instructions/', views.Instructions.as_view(), name='instructions'),
    path('order_job/', views.Order_Job.as_view(), name='order_job'),

    path('research_result/', views.ResearchResult.as_view(), name='research_result'),
    path('order_detail/<int:order_id>', views.order_detail, name='order_detail'),
    path('like/<int:order_id>', views.like, name='like'),
    path('order_submit/<int:order_id>', views.submit, name='submit'),
    path('role_choice/', views.RoleChoice.as_view(), name='role_choice'),
    path('add_role/',views.addRole, name='add_role'),
    path('add_profile/',views.addProfile,name="add_profile"),
    path('submit/',views.submit,name="submit")


]
