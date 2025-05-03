from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(LoginTable)
admin.site.register(UserTable)
admin.site.register(BudgetTable)
admin.site.register(IncomeandExpensesTable)
admin.site.register(GoalsTableCreation)
admin.site.register(SupportTable)
admin.site.register(Wallet)
admin.site.register(Category_income)
admin.site.register(Category_expence)


