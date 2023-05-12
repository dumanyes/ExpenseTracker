from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="income"),
    path('add-income', views.add_income, name="add-income"),
    path('edit-income/<int:id>', views.income_edit, name="income-edit"),
    path('income-delete/<int:id>', views.delete_income, name="income-delete"),

    path('income_category_summary_day', views.income_category_summary_day, name='income_category_summary'),

    path('stats', views.stats_view, name='income-stats'),

]