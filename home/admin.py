from django.contrib import admin
from .models import Income, Expense

# Register your models here.
# admin.site.register(Income)
# admin.site.register(Expense)

class IncomeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'category', 'amount', 'date']}),
    ]
    list_display = ('name', 'category', 'amount', 'date')
    list_filter = ['date']
    search_fields = ['name']

admin.site.register(Income, IncomeAdmin)

class ExpenseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'category', 'amount', 'date']}),
    ]
    list_display = ('name', 'category', 'amount', 'date')
    list_filter = ['date']
    search_fields = ['name']

admin.site.register(Expense, ExpenseAdmin)