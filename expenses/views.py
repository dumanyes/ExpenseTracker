from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages
from django.core.paginator import Paginator
from userpreferences.models import UserPreference
import datetime
import csv

# Create your views here.
# @login_required(login_url='/login')
def index(request):
     categories = Category.objects.all()
     expenses = Expense.objects.filter(owner=request.user)

     currency = UserPreference.objects.get(user=request.user).currency

     paginator=Paginator(expenses, 10)
     page_number = request.GET.get('page')
     page_obj = Paginator.get_page(paginator, page_number)
     context = {
          'expenses': expenses,
          'page_obj':  page_obj,
          'currency': currency,
     }
     return render(request, 'exp/index.html', context)

def add_expense(request):
     categories = Category.objects.all()
     context = {
          'categories': categories,
          'values': request.POST
     }
     if request.method == 'GET':
          return render(request, 'exp/add_expense.html', context)

     if request.method == 'POST':
          amount = request.POST['amount']

          if not amount:
               messages.error(request, 'Amount is required')
               return render(request, 'exp/add_expense.html', context)
          desrciption = request.POST['description']
          date = request.POST['expense_date']
          category = request.POST['category']

          Expense.objects.create(owner=request.user, amount=amount, date=date, description=desrciption, category=category)
          messages.success(request, 'Expense saved successfully')
          return redirect('expenses')


def expense_edit(request, id):
     expense = Expense.objects.get(pk=id)
     categories = Category.objects.all()
     context = {
          'expense': expense,
          'values': expense,
          'categories': categories
     }
     if request.method == 'GET':
          return render(request, 'exp/edit-expense.html', context)
     if request.method == 'POST':
          amount = request.POST['amount']

          if not amount:
               messages.error(request, 'Amount is required')
               return render(request, 'exp/edit-expense.html', context)
          desrciption = request.POST['description']
          date = request.POST['expense_date']
          category = request.POST['category']


          expense.owner = request.user
          expense.amount = amount
          expense.date = date
          expense.category = category
          expense.description = desrciption
          expense.save()

          messages.success(request, 'Expense updated successfully')
          return redirect('expenses')



def delete_expense(request, id):
     expense = Expense.objects.get(pk=id)
     expense.delete()
     messages.success(request, 'Expense removed')
     return redirect('expenses')


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=Expenses'+str(datetime.datetime.now())+'.csv'

    writer=csv.writer(response)
    writer.writerow(['Amount', 'Description', 'Category', 'Date'])

    expenses = Expense.objects.filter(owner=request.user)
    for expense in expenses:
        writer.writerow([expense.amount, expense.description, expense.category, expense.date])

    return response





def expense_category_summary(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date-datetime.timedelta(days=30*6)
    expenses = Expense.objects.filter(owner=request.user,
                                      date__gte=six_months_ago, date__lte=todays_date)
    finalrep = {}

    def get_category(expense):
        return expense.category
    category_list = list(set(map(get_category, expenses)))

    def get_expense_category_amount(category):
        amount = 0
        filtered_by_category = expenses.filter(category=category)

        for item in filtered_by_category:
            amount += item.amount
        return amount

    for x in expenses:
        for y in category_list:
            finalrep[y] = get_expense_category_amount(y)

    return JsonResponse({'expense_category_data': finalrep}, safe=False)








def expense_category_summary_year(request):
    todays_date = datetime.date.today()
    one_year_ago = todays_date - datetime.timedelta(days=365)  # Consider expenses from the last 365 days
    expenses = Expense.objects.filter(owner=request.user,
                                      date__gte=one_year_ago, date__lte=todays_date)
    finalrep = {}

    def get_category(expense):
        return expense.category

    category_list = list(set(map(get_category, expenses)))

    def get_expense_category_amount(category):
        amount = 0
        filtered_by_category = expenses.filter(category=category)

        for item in filtered_by_category:
            amount += item.amount
        return amount

    for x in expenses:
        for y in category_list:
            finalrep[y] = get_expense_category_amount(y)

    return JsonResponse({'expense_category_data': finalrep}, safe=False)


def expense_category_summary_month(request):
    todays_date = datetime.date.today()
    one_year_ago = todays_date - datetime.timedelta(days=30)  # Consider expenses from the last 365 days
    expenses = Expense.objects.filter(owner=request.user,
                                      date__gte=one_year_ago, date__lte=todays_date)
    finalrep = {}

    def get_category(expense):
        return expense.category

    category_list = list(set(map(get_category, expenses)))

    def get_expense_category_amount(category):
        amount = 0
        filtered_by_category = expenses.filter(category=category)

        for item in filtered_by_category:
            amount += item.amount
        return amount

    for x in expenses:
        for y in category_list:
            finalrep[y] = get_expense_category_amount(y)

    return JsonResponse({'expense_category_data': finalrep}, safe=False)


def expense_category_summary_day(request):
    todays_date = datetime.date.today()
    one_year_ago = todays_date - datetime.timedelta(days=1)  # Consider expenses from the last 365 days
    expenses = Expense.objects.filter(owner=request.user,
                                      date__gte=one_year_ago, date__lte=todays_date)
    finalrep = {}

    def get_category(expense):
        return expense.category

    category_list = list(set(map(get_category, expenses)))

    def get_expense_category_amount(category):
        amount = 0
        filtered_by_category = expenses.filter(category=category)

        for item in filtered_by_category:
            amount += item.amount
        return amount

    for x in expenses:
        for y in category_list:
            finalrep[y] = get_expense_category_amount(y)

    return JsonResponse({'expense_category_data': finalrep}, safe=False)












def stats_view(request):
    return render(request, 'exp/expense-stats.html')
