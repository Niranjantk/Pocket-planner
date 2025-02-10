from django.db import models

# Create your models here.
# Done
class LoginTable(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=10,null=True,blank=True)
    usertype=models.CharField(max_length=10,null=True,blank=True)
# wallet information
# Done
class wallet(models.Model):
    wallet_name = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    price=models.IntegerField(null=True,blank=True)
    
    
class wallet_add(models.Models):
    wallet_name = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    price=models.IntegerField(null=True,blank=True)

# user information
# Done
class UserTable(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    phoneno=models.IntegerField(null=True,blank=True)
    category=models.CharField(max_length=100,null=True,blank=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE, null=True, blank=True)
    

# budget information adding
# Done
class BudgetTable(models.Model):
   userid=models.ForeignKey(UserTable,on_delete=models.CASCADE)
   budgetname=models.CharField(max_length=100,null=True,blank=True)
   price_limit=models.IntegerField(null=True,blank=True)
   date=models.CharField(max_length=100,null=True,blank=True)
   description=models.CharField(max_length=300,null=True,blank=True)
   category=models.CharField(max_length=100,null=True,blank=True)


# income and expences information adding
# Done
class IncomeandExpencesTable(models.Model):
    userid=models.ForeignKey(UserTable,on_delete=models.CASCADE)
    wallet_name = models.CharField(LoginTable, on_delete=models.CASCADE,max_length=100,null=True,blank=True)
    amount=models.CharField(max_length=100,null=True,blank=True)
    transaction_type=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    category=models.CharField(max_length=100,null=True,blank=True)
    date=models.CharField(max_length=100,null=True,blank=True)


# goals information adding saveing money for cretain goals 
# Done
class GoalsTablecreation(models.Model):
    goal_name = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    time=models.CharField(max_length=100,null=True,blank=True)
    amount_now=models.IntegerField(null=True,blank=True)
    totalamt=models.IntegerField(null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)

class Goalshow(models.Model):
     goal_name = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
     description=models.CharField(max_length=100,null=True,blank=True)
     totalamt=models.IntegerField(null=True,blank=True)

# class BillsTable(models.Model):
#     time=models.CharField(max_length=100,null=True,blank=True)
#     amount=models.IntegerField(null=True,blank=True) 
#     description=models.CharField(max_length=100,null=True,blank=True)


# upport information adding
# Done
class SupportTable(models.Model):
    User=models.ForeignKey(LoginTable,on_delete=models.CASCADE,)
    support=models.CharField(max_length=100,null=True,blank=True) 
    reply=models.CharField(max_length=100,null=True,blank=True)


# budget alert information adding expence budget reduce expence of category
# Done
class BudgetAlertTable(models.Model):
    price=models.IntegerField(null=True,blank=True)
    date=models.CharField(max_length=100,null=True,blank=True) 
    description=models.CharField(max_length=100,null=True,blank=True)


# income and expences alert information adding
# Done
class IncomeAndExpenceAlertTable(models.Model):
    price=models.IntegerField(null=True,blank=True)
    date=models.CharField(max_length=100,null=True,blank=True) 
    description=models.CharField(max_length=100,null=True,blank=True)


# goals alert information adding
# Done
class GoalAlertTable(models.Model):
    price=models.IntegerField(null=True,blank=True)
    date=models.CharField(max_length=100,null=True,blank=True) 
    description=models.CharField(max_length=100,null=True,blank=True)



# class BillAlertTable(models.Model):
#     price=models.IntegerField(null=True,blank=True)
#     date=models.CharField(max_length=100,null=True,blank=True) 
#     description=models.CharField(max_length=100,null=True,blank=True)



# class ReviewTable(models.Model):
#     user=models.IntegerField(null=True,blank=True) 
#     message=models.CharField(max_length=100,null=True,blank=True)



# class StockTable(models.Model):
#     price=models.IntegerField(null=True,blank=True)
    

# ai chatbot information adding
# done
class AIChatbotTable(models.Model):
    sender=models.IntegerField(null=True,blank=True)
    recever=models.CharField(max_length=100,null=True,blank=True) 
    msg=models.CharField(max_length=100,null=True,blank=True)


# chart information adding
# done
class GraphAndChartTable(models.Model):
    transcactionview=models.IntegerField(null=True,blank=True)
    budgetview=models.CharField(max_length=100,null=True,blank=True) 
    goal =models.CharField(max_length=100,null=True,blank=True)
    


# class BillTable(models.Model):
#     amoun=models.IntegerField(max_length=100,null=True,blank=True)
#     time=models.CharField(max_length=100,null=True,blank=True) 



# class BillAlertTable(models.Model):
#     time=models.CharField(max_length=100,null=True,blank=True)    


class notificaton(models.Model):
    userid=models.ForeignKey(LoginTable,on_delete=models.CASCADE,)
    notificaton=models.CharField(max_length=100,null=True,blank=True)
    date=models.CharField(max_length=100,null=True,blank=True) 







    

