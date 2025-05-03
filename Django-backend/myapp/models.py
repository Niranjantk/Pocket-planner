from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver  

# User login information
class LoginTable(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=10, null=True, blank=True)
    usertype = models.CharField(max_length=10, null=True, blank=True)
    

# Wallet information
class Wallet(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    wallet_name =models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True, blank=True)

# class WalletAdd(models.Model):
#     wallet_name = models.ForeignKey(LoginTable, on_delete=models.CASCADE, related_name="wallet_adds")
#     price = models.IntegerField(null=True, blank=True)

# User information
class UserTable(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phoneno = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    LOGINID = models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True, related_name="users")
    is_active = models.BooleanField(default=True)
# Budget information
class Category_income(models.Model):
    category_name=models.CharField(max_length=100,null=True,blank=True)

class Category_expence(models.Model):
    category_name=models.CharField(max_length=100,null=True,blank=True)


class BudgetTable(models.Model):
    userid = models.ForeignKey(UserTable, on_delete=models.CASCADE, related_name="budgets")
    budgetname = models.CharField(max_length=100, null=True, blank=True)
    price_limit = models.IntegerField(null=True, blank=True)
    # date = models.CharField(max_length=100, null=True, blank=True)
    # description = models.CharField(max_length=300, null=True, blank=True)
    category = models.ForeignKey(Category_expence,on_delete=models.CASCADE, null=True, blank=True)

# Income and Expenses
class IncomeandExpensesTable(models.Model):
    LOGINID = models.ForeignKey(LoginTable, on_delete=models.CASCADE, related_name="transactions")
    wallet_name = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="transactionswallet")
    amount = models.CharField(max_length=100, null=True, blank=True)
    transaction_type = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    Category_income = models.ForeignKey(Category_income,on_delete=models.CASCADE, null=True, blank=True)
    Category_expence = models.ForeignKey(Category_expence,on_delete=models.CASCADE, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)

@receiver(post_save, sender=IncomeandExpensesTable)
def update_goal_and_budget(sender, instance, created, **kwargs):
    """
    Signal to update GoalsTableCreation when income is added
    and BudgetTable when expense is added.
    """
    if created:  # Only trigger on new entries
        amount = int(instance.amount) if instance.amount else 0  # Convert amount to integer

        # If transaction type is income, increase the goal amount
        if instance.transaction_type.lower() == "income" and instance.Category_income:
            goal = GoalsTableCreation.objects.filter(
                LOGINID=instance.LOGINID,
                category=instance.Category_income
            ).first()
            
            if goal:
                goal.totalamt = (goal.totalamt or 0) + amount
                goal.save()

        # If transaction type is expense, decrease the budget amount
        elif instance.transaction_type.lower() == "expense" and instance.Category_expence:
            # ✅ FIX: Convert LOGINID (LoginTable) to UserTable
            user = instance.LOGINID.id  # Assuming `user` is the FK in LoginTable

            budget = BudgetTable.objects.filter(
                userid=user,  # Use the mapped UserTable instance
                category=instance.Category_expence
            ).first()

            if budget:
                budget.price_limit = (budget.price_limit or 0) - amount
                budget.save()
# Goals information
class GoalsTableCreation(models.Model):
    goal_name = models.CharField(max_length=100,null=True,blank=True)
    time = models.DateTimeField(null=True, blank=True)
    amount_now = models.FloatField(null=True, blank=True)
    totalamt = models.FloatField(null=True, blank=True)
    LOGINID = models.ForeignKey(LoginTable, on_delete=models.CASCADE,null=True,blank=True, related_name="goaltransactions")
    category = models.ForeignKey(Category_income,on_delete=models.CASCADE, null=True, blank=True)
    # description = models.CharField(max_length=100, null=True, blank=True)



class GoalShow(models.Model):
    goal_name = models.ForeignKey(LoginTable, on_delete=models.CASCADE, related_name="goal_shows")
    description = models.CharField(max_length=100, null=True, blank=True)
    totalamt = models.IntegerField(null=True, blank=True)

# Support Information
class SupportTable(models.Model):
    User = models.ForeignKey(LoginTable, on_delete=models.CASCADE, related_name="supports")
    support = models.CharField(max_length=100, null=True, blank=True)
    reply = models.CharField(max_length=100, null=True, blank=True)
    support_date=models.DateField(auto_now_add=True,null=True, blank=True)

# Budget Alerts
class BudgetAlertTable(models.Model):
    price = models.IntegerField(null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

# Income and Expenses Alerts
class IncomeAndExpenseAlertTable(models.Model):
    price = models.IntegerField(null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

# Goals Alerts
class GoalAlertTable(models.Model):
    price = models.IntegerField(null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

# AI Chatbot Information
class AIChatbotTable(models.Model):
    sender = models.IntegerField(null=True, blank=True)
    receiver = models.CharField(max_length=100, null=True, blank=True)
    msg = models.CharField(max_length=100, null=True, blank=True)

# Chart Information
class GraphAndChartTable(models.Model):
    transaction_view = models.IntegerField(null=True, blank=True)
    budget_view = models.CharField(max_length=100, null=True, blank=True)
    goal = models.CharField(max_length=100, null=True, blank=True)

# Notifications
class Notification(models.Model):
    userid = models.ForeignKey(LoginTable, on_delete=models.CASCADE, related_name="notifications")
    notification = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)

