from rest_framework import serializers


from .models import *

class LoginTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginTable
        fields = '__all__'

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'
    

class UserTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = '__all__'
# budget 
class BudgetTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetTable
        fields = '__all__'

class IncomeandExpencesTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeandExpensesTable
        fields = '__all__'      
# goal
# class GoalsTableSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GoalsTable
#         fields = '__all__'

class IncomeandExpensesSerializer1(serializers.ModelSerializer):
    wallet_name = serializers.CharField(source="wallet_name.wallet_name", read_only=True)
    Category_expence_name = serializers.SerializerMethodField()
    Category_income_name = serializers.SerializerMethodField()

    class Meta:
        model = IncomeandExpensesTable
        fields = [
            "wallet_name", "amount", "transaction_type", "description",
            "Category_expence", "Category_income", "date",
            "Category_expence_name", "Category_income_name"
        ]

    def get_Category_expence_name(self, obj):
        return obj.Category_expence.category_name if obj.Category_expence else None

    def get_Category_income_name(self, obj):
        return obj.Category_income.category_name if obj.Category_income else None
class GoalsTablecreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalsTableCreation
        fields = '__all__'

class GoalshowSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalShow
        fields = '__all__'

# class BillsTableSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BillsTable
#         fields = '__all__'

class CategoryIncomeSerializer(serializers.ModelSerializer):  # Correct
    class Meta:
        model = Category_income
        fields = '__all__'

class CategoryExpenceSerializer(serializers.ModelSerializer):  # Correct
    class Meta:
        model = Category_expence
        fields = '__all__'

class SupportTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTable
        fields = '__all__'                                  

class BudgetAlertTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetAlertTable
        fields = '__all__'

class IncomeAndExpenceAlertTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeAndExpenseAlertTable
        fields = '__all__'

class GoalAlertTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalAlertTable
        fields = '__all__'

# class BillAlertTableSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BillsAlertTable
#         fields = '__all__'  


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'

# class StockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Stock
#         fields = '__all__'

# class AIChatbbotSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AIChatbbot
#         fields = '__all__'

# class GraphAndChartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GraphAndChart
#         fields = '__all__'

# # class BillTableSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = BillAlertTable
# #         fields = '__all__'

# # class BillAlertTableSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = BillAlertTable
# #         fields = '__all__'    
# 




from rest_framework import serializers
from .models import UserTable, IncomeandExpensesTable

class UserTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = '__all__'

# class IncomeandExpencesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IncomeandExpensesTable
#         fields = '__all__'
# wallet
# class WalletAddSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Wallet
#         fields = ['wallet_name', 'price','LOGIN']  # Ensure 'wallet_name' and 'user' are here


class WalletAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

class WalletAddSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'



class SupportTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTable
        fields = '__all__'  # Include all fields