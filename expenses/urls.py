from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="expenses"),
    path('add-expense', views.add_expense, name="add-expenses"),
    path('edit-expense/<int:id>', views.expense_edit, name="expense-edit"),
    path('expense-delete/<int:id>', views.delete_expense, name="expense-delete"),



    path('expoert_csv', views.export_csv, name='export-csv'),

    path('expense_category_summary', views.expense_category_summary, name='expense_category_summary'),
    path('expense_category_summary_year', views.expense_category_summary_year, name='expense_category_summary'),
    path('expense_category_summary_month', views.expense_category_summary_month, name='expense_category_summary'),
    path('expense_category_summary_day', views.expense_category_summary_day, name='expense_category_summary'),

    path('stats', views.stats_view, name='expense-stats'),


]