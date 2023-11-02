from . import views
from django.contrib import admin
from django.urls import path

app_name ='customers'

urlpatterns = [
    path('',views.customers_list,name='customers'),
    path('registeration/',views.customer_registeration,name='registeration'),
    path('customers/<int:user_id>/update/', views.customer_update, name='customer_update'),
    path('customers/<int:user_id>/Delete/',views.customer_delete,name='customer_delete'),
    path('multi_selected_delete/', views.multi_selected_delete, name='multi_selected_delete'),

    
]