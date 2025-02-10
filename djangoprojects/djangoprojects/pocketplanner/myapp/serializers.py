from rest_framework import serializers


from .models import *

class LoginTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginTable
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
        model = IncomeandExpencesTable
        fields = '__all__'      
# goal
# class GoalsTableSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GoalsTable
#         fields = '__all__'
class GoalsTablecreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalsTablecreation
        fields = '__all__'

class GoalshowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goalshow
        fields = '__all__'

# class BillsTableSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BillsTable
#         fields = '__all__'

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
        model = IncomeAndExpenceAlertTable
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
from .models import IncomeandExpencesTable

class IncomeandExpencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeandExpencesTable
        fields = '__all__'


from rest_framework import serializers
from .models import UserTable, IncomeandExpencesTable

class UserTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = '__all__'

class IncomeandExpencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeandExpencesTable
        fields = '__all__'
# wallet
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = wallet
        fields = '__all__'

class WalletAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = wallet_add
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = notificaton
        fields = '__all__'

class SupportTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTable
        fields = '__all__'