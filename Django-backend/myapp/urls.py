
from django.urls import include, path

from .views import *


from .views import UserTransactionsAPIView

urlpatterns = [
    # path('WalletAPIView',WalletAPIView.as_view(),name="WalletAPIView");
    path('WalletAddAPIView/<int:id>',WalletAPIView.as_view(),name="WalletAddAPIView"),
    path('GoalshowAPIView',GoalshowAPIView.as_view(),name="GoalshowAPIView"),
    path('',Login.as_view(),name="login"),
    path('Management_home',Management_home.as_view(),name="Management_home"),
    path('Monitoring',Monitoring.as_view(),name="Monitoring"),
     path('support/<int:complaint_id>/', support_reply, name='support_reply'),
    path('Support',Support.as_view(),name="Support"),
    path('BudgetAPIView',BudgetAPIView.as_view(),name="BudgetAPIView"),
    path('category_income',Category_incomeAPIView.as_view(),name="categoryin"),
    path('category_expence',Category_expenceAPIView.as_view(),name="categoryex"),
    path('settings',Settings.as_view(),name="settings"),
    path('About',About.as_view(),name="About"),
    path('transaction/<int:id>/',IncomeandExpensesAPIView.as_view(),name="IncomeandExpensesAPIView"),
    path('UserTransactionsAPIView/<int:id>',UserTransactionsAPIView.as_view(),name="UserTransactionsAPIView"),
    path("transactions1/<int:loginid>/", UserTransactionsAPIView1.as_view(), name="user-transactions"),
    path('GoalsTablecreationAPIView',GoalsTablecreationAPIView.as_view(),name="GoalsTablecreationAPIView"),
    path('GoalsTablecreationAPIView/<int:id>',GoalsTablecreationAPIView.as_view(),name="GoalsTablecreationAPIView"),
    path('NotificationAPIView',NotificationAPIView.as_view(),name="NotificationAPIView"),
    path('SupportTableAPIView',SupportTableAPIView.as_view(),name="SupportTableAPIView"),
    path('ViewProfileApi/<int:loginid>',ViewProfileApi.as_view(),name="ViewProfileApi"),  #//
    path('user-transactions/<int:id>', UserTransactionsAPIView.as_view(), name='user-transactions'),
    path('LoginPageApi',LoginPageApi.as_view(),name='LoginPageApi'),
    path('userregisteration',UserRegistration.as_view(),name='userregisteration'),
    # path('IncomeandExpensesindividualAPIView/<int:id>',IncomeandExpensesindividualAPIView.as_view(),name='IncomeandExpensesindividualAPIView'),
    path('FetchLoginId', FetchLoginId.as_view(), name='FetchLoginId'),
    path('getwallet/<int:loginid>', WalletsView.as_view(), name='WalletView'),  #//
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('BudgetAPIViewuser/<int:id>',BudgetAPIViewuser.as_view(),name='BudgetAPIViewuser'),
    path('GoalsTablecreationuserAPIView/<int:id>',GoalsTablecreationuserAPIView.as_view,name="GoalsTablecreationuserAPIView"),
    path('support/', SupportTableAPI.as_view()),  # GET (all) & POST
    path('support/user/<int:user_id>/', SupportTableAPI.as_view(), name="user_support_messages"),
    # path('support/<int:pk>', SupportTableAPI.as_view()),
    #   path('support/', SupportTableAPI.as_view()),   # GET (single), PUT, PATCH, DELETE

            
]
# view profile api
# wallet api