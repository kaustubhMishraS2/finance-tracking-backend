from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

# Transaction API
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):# Filter transactions by logged-in user
        user = self.request.user
        queryset = Transaction.objects.filter(user=user)

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__iexact=category)

        type = self.request.query_params.get('type')
        if type:
            queryset = queryset.filter(type=type)

        return queryset
    
# Summary API
    @action(detail=False, methods=['get'])
    def summary(self, request):
        transactions = Transaction.objects.filter(user=request.user)

        income = sum(t.amount for t in transactions if t.type == 'income')
        expense = sum(t.amount for t in transactions if t.type == 'expense')

        return Response({
            "total_income": income,
            "total_expense": expense,
            "balance": income - expense
        })


# User registration API

@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        return Response({
            "message": "Send POST request with username and password to register",
             "example": {
                "username": "your_username",
                "password": "your_password"
            },
            "note": "Copy the example JSON below and replace values"
        })

    username = request.data.get('username')
    password = request.data.get('password')

    # Empty validation
    if not username or not password:
        return Response(
            {"error": "Username and password are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Password length check
    if len(password) < 4:
        return Response(
            {"error": "Password must be at least 4 characters long"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Duplicate user check
    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "User already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Create user
    user = User.objects.create_user(username=username, password=password)

    return Response(
        {"message": "User created successfully"},
        status=status.HTTP_201_CREATED
    )