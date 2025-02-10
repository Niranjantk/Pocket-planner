from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(LoginTable)
admin.site.register(UserTable)
admin.site.register(BudgetTable)
admin.site.register(IncomeandExpencesTable)
admin.site.register(GoalsTable)
admin.site.register(SupportTable)

