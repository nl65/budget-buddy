from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from .models import Income, Expense
from django.template import loader

# Create your views here.

def index(request):
    context = {
        'incomes': Income.objects.all(),
        'expenses': Expense.objects.all()
    }
    return render(request, 'home/index.html', context)

def incomes(request):
    incomes = Income.objects.all()
    context = {
        'incomes': incomes
    }
    return render(request, 'home/incomes.html', context)

def expenses(request):
    expenses = Expense.objects.all()
    context = {
        'expenses': expenses
    }
    return render(request, 'home/expenses.html', context)

def expense_stats(request):
    '''
    create dictionary of all expense/income categories' totals
    '''
    expenses = Expense.objects.all()
    totals = {'Food': 0,
              'Travel': 0,
              'Shopping': 0,
              'Necessities': 0,
              'Entertainment': 0,
              'Subscriptions': 0,
              'Other': 0 }
    for expense in expenses:
        if expense.category == 'Food':
            totals["Food"] += expense.amount
        elif expense.category == 'Travel':
            totals["Travel"] += expense.amount
        elif expense.category == 'Shopping':
            totals["Shopping"] += expense.amount
        elif expense.category == 'Necessities':
            totals["Necessities"] += expense.amount
        elif expense.category == 'Entertainment':
            totals["Entertainment"] += expense.amount
        elif expense.category == 'Subscriptions':
            totals["Subscriptions"] += expense.amount
        elif expense.category == 'Other':
            totals["Other"] += expense.amount

    incomes = Income.objects.all()
    totals_incomes = {'Work': 0, 'Other': 0}
    for income in incomes:
        if income.category == 'Work':
            totals_incomes["Work"] += income.amount
        elif income.category == 'Other':
            totals_incomes["Other"] += income.amount
     
    context = {
        'totals': sum(totals.values()),
        'food_amt': totals["Food"],
        'travel_amt': totals["Travel"],
        'shopping_amt': totals["Shopping"],
        'necessities_amt': totals["Necessities"],
        'entertainment_amt': totals["Entertainment"],
        'subscriptions_amt': totals["Subscriptions"],
        'other_amt': totals["Other"],
        'totals_incomes': sum(totals_incomes.values()),
        'work_amt_incomes': totals_incomes["Work"],
        'other_amt_incomes': totals_incomes["Other"]
    }
    return render(request, 'home/summary.html', context)

def expense_past_month(request):
    '''
    Get sum of all expenses over the past month
    '''
    return

def summary(request):
    return HttpResponse("Unfinished Charts page")