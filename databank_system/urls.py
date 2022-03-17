from databank_system import views
from django.urls import path

app_name = 'databank_system'

urlpatterns = [
    # homepage url, mobile menu
    path('mobile_menu/', views.mobile_menu, name='mobile_menu'),
    path('', views.home_page, name='home_page'),
    # record urls
    path('single_record_edit/<id>/', views.single_record_edit, name='single_record_edit'),
    path('all_records/', views.all_records_default, name='all_records_default'),
    path('all_records/<order_by>/', views.all_records, name='all_records'),
    path('delete_record/<id>/', views.delete_record, name='delete_record'),
    path('single_record/<id>/', views.single_record, name='single_record'),
    path('new_record/', views.new_record, name='new_record'),
    # billing urls
    path('single_billing_edit/<id>/', views.single_billing_edit, name='single_billing_edit'),
    path('all_billings/', views.all_billings_default, name='all_billings_default'),
    path('all_billings/<order_by>/', views.all_billings, name='all_billings'),
    path('delete_billing/<id>/', views.delete_billing, name='delete_billing'),
    path('export_billing/<id>/', views.export_billing, name='export_billing'),
    path('single_billing/<id>/', views.single_billing, name='single_billing'),
    path('new_billing/', views.new_billing, name='new_billing'),
    # user urls
    path('delete_user/<username>/', views.delete_user, name='delete_user'),
    path('registration/', views.registration, name='registration'),
    path('users/', views.users, name='users'),
    # login, logout
    path('logout/', views.user_logout, name='user_logout'),
    path('login/', views.user_login, name='user_login'),
]
