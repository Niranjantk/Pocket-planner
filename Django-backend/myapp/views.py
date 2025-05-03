from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from myapp.models import LoginTable, UserTable
from .serializers import *
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
# from .forms import ForgotPasswordForm


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
    def get(self, request):
        categories = ["Business", "Student", "Job", "Others"]
        
        # Fetch user count dynamically
        user_counts = {category: UserTable.objects.filter(category=category).count() for category in categories}

        total_users = UserTable.objects.count()

        return render(request, "Management_page.html", {
            "usercount": total_users,
            "user_counts": user_counts,
            "categories": list(user_counts.keys()),   # Pass category names
            "counts": list(user_counts.values())     # Pass user count values
        })
        
class Monitoring(View):
        def get(self,request):
            user_instance = UserTable.objects.all()
            return render(request,"Monitoring_page.html",{'user_instance':user_instance})

class About(View):
        def get(self,request):
            return render(request,"About_page.html")

class Support(View):
        def get(self,request):
            sup=SupportTable.objects.all()
            return render(request,"Support_page.html",{'obj':sup})
         

class Settings(View):
        def get(self,request):
            return render(request,"settings_page.html")                                

# apis
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SupportTable  # Import your Support model

@csrf_exempt  # Use only if you are not handling CSRF properly in frontend
def support_reply(request, complaint_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse JSON data
            reply_text = data.get("reply")

            if not reply_text:
                return JsonResponse({"error": "Reply cannot be empty"}, status=400)

            support_obj = get_object_or_404(SupportTable, id=complaint_id)  # Get the complaint object
            support_obj.reply = reply_text  # Update the reply field
            support_obj.save()  # Save to database

            return JsonResponse({"message": "Reply saved successfully", "reply": reply_text})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)




class LoginPageApi(APIView):
    def post(self, request):
        response_dict= {}
        password = request.data.get("password")
        print("Password ------------------> ",password)
        username = request.data.get("username")
        print("Username ------------------> ",username)
        try:
            user = LoginTable.objects.filter(username=username, password=password).first()
            print("user_obj :-----------", user)
        except Login.DoesNotExist:
            response_dict["message"] = "No account found for this username. Please signup."
            return Response(response_dict, HTTP_200_OK)
      
        if user.usertype == "user":
            response_dict = {
                "login_id": user.id  ,
                "user_type": user.usertype,
                "status": "success",
                "username":user.username,
                "email":user.username,
            }   
            print("User details :--------------> ",response_dict)
            return Response(response_dict, HTTP_200_OK)
        else:
            response_dict["message "] = "ok"
            return Response(response_dict, HTTP_200_OK)




from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

class UserRegistration(APIView):

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
            password = request.data['password']
            login_profile = login_serial.save(usertype='user', password=password)
            user_instance = user_serial.save(LOGINID=login_profile)

            # Prepare login response
            login_data = {
                'login_id': login_profile.id,
                'username': login_profile.username,
                'user_type': login_profile.usertype
            }

            # Respond with user and login details
            return Response({
               
                'login': login_data
            }, status=HTTP_201_CREATED)

        # Log detailed errors for debugging
        print("User Serializer Errors:", user_serial.errors)
        print("Login Serializer Errors:", login_serial.errors)

        # Return validation errors
        return Response({
            'login_error': login_serial.errors if not login_valid else None,
            'user_error': user_serial.errors if not data_valid else None
        }, status=HTTP_400_BAD_REQUEST)


class FetchLoginId(APIView):
    def get(self, request):
        pass

from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

class IncomeandExpensesAPIView(APIView):
    def post(self, request, id):
        # amount= request.data.get('amount')
        # LOGINID= request.data.get('LOGINID')
        # print('----------lid---->', LOGINID)
        # # b_obj = BudgetTable.objects.get(userid__LOGINID_id=LOGINID)
        # print('--------amount------', amount)
        # budject_amount = b_obj.price_limit
        # print('-------budject_amount-------', budject_amount)
        # balance = budject_amount-amount
        # b_obj.price_limit=balance
        # print('--------balance------', balance)
        # b_obj.save()



        print(request.data)
        try:
            # Retrieve user instance

            user = LoginTable.objects.get(id=id)

            # Retrieve wallet instance for the user
            wallet = Wallet.objects.filter(LOGIN=user).first()  # Assuming one wallet per user

            if not wallet:
                return Response({"error": "Wallet not found for this user"}, status=HTTP_400_BAD_REQUEST)
            data={}
            data=request.data
            # # Add user and wallet to request data
            if request.data['transaction_type']=='Income':
                data['Category_income']=request.data['category']
            else:
                data['Category_expence']=request.data['category']
        
            # request_data = request.data.copy()
            data["LOGINID"] = user.id
            data["wallet_name"] = wallet.id

            # Serialize and save the data
            print(data)
            serializer = IncomeandExpencesTableSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        except LoginTable.DoesNotExist:
            return Response({"error": "User not found"}, status=HTTP_400_BAD_REQUEST)

    












# class IncomeandExpensesindividualAPIView(APIView):  #//
#     def get(self, request,id):
#         transactions = IncomeandExpensesTable.objects.filter(userid__LOGINID__id=id).all()
#         serializer = IncomeandExpencesSerializer(transactions, many=True)
#         return Response(serializer.data, status=HTTP_200_OK)
    

# =========================//
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IncomeandExpensesTable, UserTable
from collections import defaultdict

# class UserTransactionsAPIView1(APIView):
#     def get(self, request, loginid):
#         try:
#             # Check if user exists
#             user = LoginTable.objects.get(id=loginid)

#             # Fetch transactions related to the user
#             transactions = IncomeandExpensesTable.objects.filter(LOGINID=user).order_by("date")

#             if not transactions.exists():
#                 return Response({"message": "No transactions found for this user"}, status=HTTP_200_OK)

#             # Serialize transactions
#             serialized_data = IncomeandExpensesSerializer1(transactions, many=True).data

#             # Group transactions by date
#             grouped_data = defaultdict(list)
#             for item in serialized_data:
#                 grouped_data[item["date"]].append(item)

#             # Format the final JSON response
#             response_data = [{"date": date, "data": data} for date, data in grouped_data.items()]

#             return Response(response_data, status=HTTP_200_OK)

#         except LoginTable.DoesNotExist:
#             return Response({"error": "User not found"}, status=HTTP_400_BAD_REQUEST)

class UserTransactionsAPIView1(APIView):
    def get(self, request, loginid):
        try:
            # Check if user exists
            user = LoginTable.objects.get(id=loginid)

            # Fetch transactions related to the user, ordered by date (descending)
            transactions = IncomeandExpensesTable.objects.filter(LOGINID=user).order_by("-date", "-id")

            if not transactions.exists():
                return Response({"message": "No transactions found for this user"}, status=HTTP_200_OK)

            # Serialize transactions
            serialized_data = IncomeandExpensesSerializer1(transactions, many=True).data

            # Group transactions by date, ensuring LIFO order (latest transactions first)
            grouped_data = defaultdict(list)
            for item in serialized_data:
                grouped_data[item["date"]].insert(0, item)  # Insert at the beginning to maintain LIFO order

            # Format the final JSON response (dates are already in descending order)
            response_data = [{"date": date, "data": data} for date, data in grouped_data.items()]

            return Response(response_data, status=HTTP_200_OK)

        except LoginTable.DoesNotExist:
            return Response({"error": "User not found"}, status=HTTP_400_BAD_REQUEST)
        
class UserTransactionsAPIView(APIView):
    def get(self, request, id):
        print(request.data)
        users = UserTable.objects.filter(LOGINID__id=id).first()
        response_data = []

        if users:
            transactions = IncomeandExpensesTable.objects.filter(LOGINID__id=id)
            income = sum(int(t.amount) for t in transactions if t.transaction_type == "Income" and t.amount.strip().isdigit())

            expense = sum(int(t.amount) for t in transactions if t.transaction_type == "Expense" and t.amount.strip().isdigit())
            balance = income - expense

            all_transactions = [
                {
                    "wallet_name": t.wallet_name.wallet_name,  # Assuming Wallet has a 'name' field
                    "amount": t.amount,
                    "transaction_type": t.transaction_type,
                    "description": t.description,
                    # "category": t.category,
                    "date": t.date,
                }
                for t in transactions
            ]

            user_data = {
                "username": users.LOGINID.username,
                "email": users.email,
                "image": "",  # Add logic for image if applicable
                "transactions": {"income": income, "expense": expense},
                "balance amount": balance,
                "alltransactions": all_transactions  # Adding all transactions here
            }
            response_data.append(user_data)

        return Response(response_data, status=status.HTTP_200_OK)

# =========================

class Category_incomeAPIView(APIView):
    def get(self, request):
        budgets = Category_income.objects.all()
        serializer = CategoryIncomeSerializer(budgets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Category_expenceAPIView(APIView):
    def get(self, request):
        budgets = Category_expence.objects.all()
        serializer = CategoryExpenceSerializer(budgets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# budget class//
class BudgetAPIViewuser(APIView):
    def get(self, request,id):
        budgets = BudgetTable.objects.filter(userid__LOGINID__id=id).all()
        serializer = BudgetTableSerializer(budgets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BudgetAPIView(APIView):
    def get(self, request):
        budgets = BudgetTable.objects.all()
        serializer = BudgetTableSerializer(budgets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data={}
        data=request.data
        data['userid']=UserTable.objects.get(LOGINID__id=request.data['userid']).id
        print(data)
        serializer = BudgetTableSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# =======================
# wallet page//

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class WalletAPIView(APIView):
    def post(self, request, id):  # Accept LOGINID from URL
        """
        Add an entry to a specific wallet.
    
        """
        print(request.data)
        # Validate if LOGINID exists in LoginTable
        login_instance = get_object_or_404(LoginTable, id=id)

        # Attach LOGINID to request data before serialization
        request.data['LOGIN'] = login_instance.id  

        # Serialize data
        serializer = WalletAddSerializer(data=request.data)

        # Debugging print statements
        print("Received Data:", request.data)
        print("Serializer Valid?", serializer.is_valid())

        if serializer.is_valid():
            serializer.save(LOGIN=login_instance)  # Save with LOGINID
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print("Serializer Errors:", serializer.errors)  # Log errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







# =================================
# wallet creation//
# class WalletAddAPIView(APIView):
#     def get(self, request):
#         wallet_adds = WalletAdd.objects.all()
#         serializer = WalletAddSerializer(wallet_adds, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = WalletAddSerializer(data=request.data)
#         print('------------------>', request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# =============================================
# goal view//
class GoalshowAPIView(APIView):
    def get(self, request):
        goals = GoalShow.objects.all()
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

class GoalsTablecreationuserAPIView(APIView):
    def get(self, request):
        goals = GoalsTableCreation.objects.all()
        serializer = GoalsTablecreationSerializer(goals,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GoalsTablecreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GoalsTablecreationAPIView(APIView):
    def get(self, request,id=None):
        if id:
            goals = GoalsTableCreation.objects.filter(LOGINID__id=id).all()
            serializer = GoalsTablecreationSerializer(goals,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            goals = GoalsTableCreation.objects.all()
            serializer = GoalsTablecreationSerializer(goals,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data={}
        data=request.data
        print(request.data)
        data['totalamt']=0
        serializer = GoalsTablecreationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ========================================
# notification//
class NotificationAPIView(APIView):
    def get(self, request):
        notifications = Notification.objects.all()
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
    def get(self, request, loginid):
        print(request.data)
        print("here")
        obj = UserTable.objects.filter(LOGINID=loginid)
        serializer = UserTableSerializer(obj, many = True)
        print("time----------------> ", serializer.data)
        return Response(serializer.data)


class WalletsView(APIView):
    def get(self, request, loginid):
        try:
            # Check if user exists
            # user = LoginTable.objects.get(id=loginid)
            try:
            # Fetch transactions related to the user
                wallets = Wallet.objects.get(LOGIN__id=loginid)
            except Wallet.DoesNotExist:
            
                return Response({"message": "No wallets found for this user"}, status=HTTP_200_OK)

            # Serialize transactions
            serialized_data = WalletSerializer(wallets)

            # Group transactions by date    
            # grouped_data = defaultdict(list)
            # for item in serialized_data:
            #     grouped_data[item["date"]].append(item)

            # # Format the final JSON response
            # response_data = [{"date": date, "data": data} for date, data in grouped_data.items()]

            return Response(serialized_data.data, status=HTTP_200_OK)

        except LoginTable.DoesNotExist:
            return Response({"error": "User not found"}, status=HTTP_400_BAD_REQUEST)
        
class ForgotPasswordView(APIView):


    def post(self, request, *args, **kwargs):
        
        
            email = request.data['email']
            print(email)
            
            try:
                print("hhhhhh")
                user = UserTable.objects.get(email=email)
                print(user)  # Fetch user based on email
                user_password = user.LOGINID.password  # Get the password hash (you won't send plain password)
                # print(user)
                # You should ideally send a password reset link instead of the plain password
                subject = "Password Reset"
                message = f"Your password is: {user_password}"  # This is just an example; sending the plain password is not recommended
                from_email = "no-reply@yourdomain.com"
                recipient_list = [email]
                
                send_mail(subject, message, from_email, recipient_list)
                return Response({"message":"password sent sucessfully"}, status=status.HTTP_200_OK)
                # Redirect to the login page

            except LoginTable.DoesNotExist:
                return Response({"error": "User not found"}, status=HTTP_400_BAD_REQUEST)
            

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import SupportTable
from .serializers import SupportTableSerializer

class SupportTableAPI(APIView):

    def get(self, request, pk=None):
        """Handles GET requests - Fetch all or a single Support Record"""
        if pk:
            support = get_object_or_404(SupportTable, pk=pk)
            serializer = SupportTableSerializer(support)
        else:
            support = SupportTable.objects.all()
            serializer = SupportTableSerializer(support, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        """Handles POST request (Create a new support entry)"""
        serializer = SupportTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request, user_id):
        """Fetch all support messages sent by a specific user"""
        try:
            # Filter support messages by the given user ID
            messages = SupportTable.objects.filter(User=user_id).order_by("-support_date")

            # Check if any messages exist
            if not messages.exists():
                return Response({"message": "No messages found for this user"}, status=status.HTTP_404_NOT_FOUND)

            # Serialize the messages
            serializer = SupportTableSerializer(messages, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def post(self, request,pk):
    #     """Handles POST request - Create a new Support Record"""
    #     serializer = SupportTableSerializer(data=request.data)
    #     print(serializer)
    #     if serializer.is_valid():
    #         serializer.User=pk
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk):
    #     """Handles PUT request - Update an Entire Support Record"""
    #     support = get_object_or_404(SupportTable, pk=pk)
    #     serializer = SupportTableSerializer(support, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request, pk):
    #     """Handles PATCH request - Partially Update a Support Record"""
    #     support = get_object_or_404(SupportTable, pk=pk)
    #     serializer = SupportTableSerializer(support, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Handles DELETE request - Delete a Support Record"""
        support = get_object_or_404(SupportTable, pk=pk)
        support.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

            




        