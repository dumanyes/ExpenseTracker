from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request, 'exp/index.html')

def add_expense(request):
     return render(request, 'exp/add_expense.html')
