from django.urls import path

from . import views

# 127.0.0.1:8000/home/...

urlpatterns = [
    path('', views.index, name = 'index'),
    path('incomes/', views.incomes, name = 'incomes'),
    path('expenses/', views.expenses, name = 'expenses'),
    path('summary/', views.expense_stats, name = 'summary'),
]