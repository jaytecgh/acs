from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from django.contrib.auth import authenticate, get_user_model, logout as django_logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.shortcuts import get_object_or_404
from database.models import Employee
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from database.serializers import MyTokenObtainPairSerializer



User = get_user_model()

@api_view(['POST'])
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    full_name = request.data.get('full_name')

    if not all([email, password, full_name]):
        return Response({'error': 'All fields are required.'}, status=400)

    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already registered.'}, status=400)

    user = User.objects.create_user(email=email, password=password)
    user.is_active = True
    user.save()
    Employee.objects.create(user=user, full_name=full_name)


    return Response({'message': 'Account created. Please wait for admin approval.'}, status=201)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = serializers.EmailField()
        self.fields['password'] = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'), email=email, password=password)

        if not user:
            raise serializers.ValidationError('Invalid email or password.')

        self.user = user
        employee = getattr(user, 'employee', None)
        if not employee or not employee.role:
            raise serializers.ValidationError('Your account is pending approval.')

        data = super().validate(attrs)
        data['user'] = {
            'id': user.id,
            'email': user.email,
            'role': employee.role,
            'can_edit': employee.can_edit,
            'can_delete': employee.can_delete,
        }
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')
    if not email:
        return Response({"error": "Email is required."}, status=400)

    try:
        user = User.objects.get(email=email)
        token = default_token_generator.make_token(user)
        reset_link = f"https://acs-chi.vercel.app/reset-password/{token}"

        send_mail(
            subject="Password Reset Request",
            message=f"Hi, click the link to reset your password: {reset_link}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )

        return Response({"message": "Reset link sent to email."}, status=200)

    except User.DoesNotExist:
        return Response({"error": "No user found with that email."}, status=404)


@api_view(['POST'])
def reset_password(request):
    token = request.data.get("token")
    password = request.data.get("password")
    email = request.data.get("email")

    if not all([token, password, email]):
        return Response({"error": "Token, email, and password required."}, status=400)

    user = get_object_or_404(User, email=email)
    if not default_token_generator.check_token(user, token):
        return Response({"error": "Invalid or expired token."}, status=400)

    user.set_password(password)
    user.save()
    return Response({"message": "Password reset successful."})


@api_view(['POST'])
def logout_view(request):
    try:
        refresh_token = request.data.get("refresh")
        token = RefreshToken(refresh_token)
        token.blacklist()
        django_logout(request)
        return Response({"message": "Logout successful."})
    except Exception:
        return Response({"error": "Logout failed."}, status=400)
