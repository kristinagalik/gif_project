from django.urls import path
from databank_system import views

app_name = 'databank_system'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('all_records/', views.all_records, name='all_records'),
    path('new_record/', views.new_record, name='new_record'),
    path('record/', views.record, name='record'),  # TODO -> dynamic numbering (slugs)
    path('all_billings/', views.all_billings, name='all_billings'),
    path('new_billing/', views.new_billing, name='new_billing'),
    path('billing/', views.billing, name='billing'),  # TODO -> dynamic numbering (slugs)
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
