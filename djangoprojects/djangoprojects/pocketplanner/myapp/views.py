from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from myapp.models import LoginTable, UserTable
from.serializers import *

# Create your views here.

class Login(View):
    def get(self,request):
        return render(request,"Login_page.html")
    
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            login_obj = LoginTable.objects.get(username=username,password=password)
            if login_obj.usertype == "admin":
                return HttpResponse('''<script>alert("Welcome Admin");window.location="/Management_home"</script>''')
        except:
            return HttpResponse('''<script>alert("Invalid Username or Password");window.location="/"</script>''')
class Management_home(View):
        def get(self,request):
            return render(request,"Management_page.html")
        
class Monitoring(View):
        def get(self,request):
            user_instance = UserTable.objects.all()
            return render(request,"Monitoring_page.html",{'user_instance':user_instance})

class About(View):
        def get(self,request):
            return render(request,"About_page.html")

class Support(View):
        def get(self,request):
            return render(request,"Support_page.html") 

class Settings(View):
        def get(self,request):
            return render(request,"settings_page.html")                                

# apis

class LoginPageApi(APIView):
    def post(self, request):
        response_dict= {}
        password = request.data.get("password")
        print("Password ------------------> ",password)
        username = request.data.get("username")
        print("Username ------------------> ",username)
        try:
            user = Login.objects.filter(Username=username, Password=password).first()
            print("user_obj :-----------", user)
        except Login.DoesNotExist:
            response_dict["message"] = "No account found for this username. Please signup."
            return Response(response_dict, HTTP_200_OK)
      
        if user.Type == "student":
            response_dict = {
                "login_id": str(user.id),
                "user_type": user.Type,
                "status": "success",
            }   
            print("User details :--------------> ",response_dict)
            return Response(response_dict, HTTP_200_OK)
        else:
            response_dict["message "] = "Your account has not been approved yet or you are a CLIENT user."
            return Response(response_dict, HTTP_200_OK)




class userregisteration(APIView):

    def post(self, request):
        """
        Handle student registration.
        """
        print("###############", request.data)
        
        # Serialize user and login data
        user_serial = UserTableSerializer(data=request.data)
        login_serial = LoginTableSerializer(data=request.data)
        
        # Validate the serializers
        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            print("&&&&&&&&&&&&&&&&& Data is valid")
            
            # Save login and user data
            password = request.data['Password']
            department = request.data['department']
            login_profile = login_serial.save(Type='user', Password=password)
            user_serial.save(LOGIN=login_profile)
            
            # Respond with the serialized user data
            return Response(user_serial.data, status=HTTP_201_CREATED)

        # Log detailed errors for debugging
        print("User Serializer Errors:", user_serial.errors)
        print("Login Serializer Errors:", login_serial.errors)

        # Return validation errors
        return Response({
            'login_error': login_serial.errors if not login_valid else None,
            'user_error': user_serial.errors if not data_valid else None
        }, status=HTTP_400_BAD_REQUEST)

class IncomeandExpensesAPIView(APIView):  #//
    def get(self, request):
        transactions = IncomeandExpencesTable.objects.all()
        serializer = IncomeandExpencesSerializer(transactions, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = IncomeandExpencesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
class IncomeandExpensesindividualAPIView(APIView):  #//
    def get(self, request,id):
        transactions = IncomeandExpencesTable.objects.filter(userid__LOGINID__id=id).all()
        serializer = IncomeandExpencesSerializer(transactions, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    

# =========================//
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IncomeandExpencesTable, UserTable
from .serializers import IncomeandExpencesSerializer, UserTableSerializer

class UserTransactionsAPIView(APIView):
    def get(self, request):
        users = UserTable.objects.all()
        response_data = []

        for user in users:
            transactions = IncomeandExpencesTable.objects.filter(userid=user)
            income = sum(int(t.amount) for t in transactions if t.transaction_type == "income")
            expense = sum(int(t.amount) for t in transactions if t.transaction_type == "expense")
            balance = income - expense

            user_data = {
                "username": user.username,
                "email": user.email,
                "image": "",  # Add logic for image if applicable
                "transactions": [{"income": income, "expense": expense}],
                "balance amount": balance
            }
            response_data.append(user_data)

        return Response(response_data, status=status.HTTP_200_OK)
# =========================

# budget class//

class BudgetAPIView(APIView):
    def get(self, request):
        budgets = BudgetTable.objects.all()
        serializer = BudgetTableSerializer(budgets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BudgetTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# =======================
# wallet page//

class WalletAPIView(APIView):
    def get(self, request):
        wallets = wallet.objects.all()
        serializer = WalletSerializer(wallets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WalletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# =================================
# wallet creation//
class WalletAddAPIView(APIView):
    def get(self, request):
        wallet_adds = wallet_add.objects.all()
        serializer = WalletAddSerializer(wallet_adds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WalletAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# =============================================
# goal view//
class GoalshowAPIView(APIView):
    def get(self, request):
        goals = Goalshow.objects.all()
        serializer = GoalshowSerializer(goals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GoalshowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ================================
# goal creaation//
class GoalsTablecreationAPIView(APIView):
    def get(self, request):
        goals = GoalsTablecreation.objects.all()
        serializer = GoalsTablecreationSerializer(goals,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GoalsTablecreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ========================================
# notification//
class NotificationAPIView(APIView):
    def get(self, request):
        notifications = notificaton.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# =============================
# support//
class SupportTableAPIView(APIView):
    def get(self, request):
        supports = SupportTable.objects.all()
        serializer = SupportTableSerializer(supports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SupportTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# =======================================

# //
class ViewProfileApi(APIView):
    def get(self, request, lid):
        obj = UserTable.objects.filter(LOGIN_id=lid)
        serializer = UserTableSerializer(obj, many = True)
        print("time----------------> ", serializer)
        return Response(serializer.data)


