from django.urls import path
from databank_system import views

app_name = 'databank_system'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('all_records/<order_by>/', views.all_records, name='all_records'),
    path('all_records/', views.all_records_default, name='all_records_default'),
    path('new_record/', views.new_record, name='new_record'),
    path('single_record/<id>/', views.single_record, name='single_record'),
    path('single_record_edit/<id>/', views.single_record_edit, name='single_record_edit'),
    path('delete_record/<id>/', views.delete_record, name='delete_record'),
    path('all_billings/<order_by>/', views.all_billings, name='all_billings'),
    path('all_billings/', views.all_billings_default, name='all_billings_default'),
    path('new_billing/', views.new_billing, name='new_billing'),
    path('single_billing/<id>', views.single_billing, name='single_billing'),
    path('single_billing_edit/<id>/', views.single_billing_edit, name='single_billing_edit'),
    path('delete_billing/<id>/', views.delete_billing, name='delete_billing'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
