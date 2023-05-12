import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Source, UserIncome
from django.contrib import messages
from django.core.paginator import Paginator
from userpreferences.models import UserPreference

# Create your views here.
@login_required(login_url='authentication/login')
def index(request):
     categories = Source.objects.all()
     income = UserIncome.objects.filter(owner=request.user)

     currency = UserPreference.objects.get(user=request.user).currency

     paginator=Paginator(income, 10)
     page_number = request.GET.get('page')
     page_obj = Paginator.get_page(paginator, page_number)
     context = {
          'income': income,
          'page_obj':  page_obj,
          'currency': currency,
     }
     return render(request, 'income/index.html', context)

def add_income(request):
     sources = Source.objects.all()
     context = {
          'sources': sources,
          'values': request.POST
     }
     if request.method == 'GET':
          return render(request, 'income/add_income.html', context)

     if request.method == 'POST':
          amount = request.POST['amount']

          if not amount:
               messages.error(request, 'Amount is required')
               return render(request, 'income/add_income.html', context)
          desrciption = request.POST['description']
          date = request.POST['income_date']
          source = request.POST['source']

          UserIncome.objects.create(owner=request.user, amount=amount, date=date, description=desrciption, source=source)
          messages.success(request, 'Record saved successfully')
          return redirect('income')


def income_edit(request, id):
     income = UserIncome.objects.get(pk=id)
     sources = Source.objects.all()
     context = {
          'income': income,
          'values': income,
          'sources': sources
     }
     if request.method == 'GET':
          return render(request, 'income/edit-income.html', context)
     if request.method == 'POST':
          amount = request.POST['amount']

          if not amount:
               messages.error(request, 'Amount is required')
               return render(request, 'income/edit-income.html', context)
          desrciption = request.POST['description']
          date = request.POST['income_date']
          source = request.POST['source']


          income.owner = request.user
          income.amount = amount
          income.date = date
          income.source = source
          income.description = desrciption
          income.save()

          messages.success(request, 'Record updated successfully')
          return redirect('income')



def delete_income(request, id):
     income = UserIncome.objects.get(pk=id)
     income.delete()
     messages.success(request, 'Record removed')
     return redirect('income')


def stats_view(request):
    return render(request, 'income/income-stats.html')









def income_category_summary_day(request):
    todays_date = datetime.date.today()
    one_year_ago = todays_date - datetime.timedelta(days=1)  # Consider expenses from the last 365 days
    incomes = UserIncome.objects.filter(owner=request.user,
                                      date__gte=one_year_ago, date__lte=todays_date)
    finalrep = {}

    def get_category(userincome):
        return userincome.source

    category_list = list(set(map(get_category, incomes)))

    def get_income_category_amount(source):
        amount = 0
        filtered_by_category = incomes.filter(source=source)

        for item in filtered_by_category:
            amount += item.amount
        return amount

    for x in incomes:
        for y in category_list:
            finalrep[y] = get_income_category_amount(y)

    return JsonResponse({'income_category_data': finalrep}, safe=False)



