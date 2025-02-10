
from django.urls import include, path

from .views import *


from .views import UserTransactionsAPIView

urlpatterns = [
    # path('WalletAPIView',WalletAPIView.as_view(),name="WalletAPIView");
    path('WalletAddAPIView',WalletAddAPIView.as_view(),name="WalletAddAPIView"),
    path('GoalshowAPIView',GoalshowAPIView.as_view(),name="GoalshowAPIView"),
    path('',Login.as_view(),name="login"),
    path('Management_home',Management_home.as_view(),name="Management_home"),
    path('Monitoring',Monitoring.as_view(),name="Monitoring"),
    path('Support',Support.as_view(),name="Support"),
    path('BudgetAPIView',BudgetAPIView.as_view,name="BudgetAPIView"),
    path('settings',Settings.as_view(),name="settings"),
    path('About',About.as_view(),name="About"),
    path('IncomeandExpensesAPIView',IncomeandExpensesAPIView.as_view(),name="IncomeandExpensesAPIView"),
    path('UserTransactionsAPIView',UserTransactionsAPIView.as_view(),name="UserTransactionsAPIView"),
    path('GoalsTablecreationAPIView',GoalsTablecreationAPIView.as_view(),name="GoalsTablecreationAPIView"),
    path('NotificationAPIView',NotificationAPIView.as_view(),name="NotificationAPIView"),
    path('SupportTableAPIView',SupportTableAPIView.as_view(),name="SupportTableAPIView"),
    path('ViewProfileApi',ViewProfileApi.as_view(),name="ViewProfileApi"),
    path('user-transactions/', UserTransactionsAPIView.as_view(), name='user-transactions'),
    path('LoginPageApi',LoginPageApi.as_view(),name='LoginPageApi'),
    path('userregisteration',userregisteration.as_view(),name='userregisteration'),
    path('IncomeandExpensesindividualAPIView/<int:id>',IncomeandExpensesindividualAPIView.as_view(),name='IncomeandExpensesindividualAPIView'),
 
]
