from . import views
from django.urls import path

app_name ='finance'

urlpatterns = [
    path('',views.transactions_view,name='transactions'),
    path('registeration/',views.transaction_register,name='registeration'),
    path('transaction/<int:transaction_id>/update/',views.transaction_update,name='update'),
    path('transaction/<int:transaction_id>/delete/',views.transaction_delete,name='delete'),
    path('multi_selected_delete',views.multi_selected_delete,name='multi_selected_delete'),
    path('financial data/',views.dashboard_view,name='financial_data'),
    path('yearly data/',views.yearly_report,name='yearly_report'),
    path('payments/',views.payments,name='payments')


    
]