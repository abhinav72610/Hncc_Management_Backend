from re import U
from django.db.models.query import QuerySet
from .models import NewUser, Profile
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, ProfileSerializer, EmailVerificationSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from rest_framework import permissions
from .models import NewUser
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework import views
import jwt
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                user_data = serializer.data
                user_instance = NewUser.objects.get(email=user_data['email'])
                token = RefreshToken.for_user(user_instance).access_token
                # current_site = get_current_site(request).domain
                # relativeLink = reverse('email-verify')
                # relativeLink = 'email-verify'
                # absurl = 'http://'+current_site + \
                #     relativeLink+"?token="+str(token)
                absurl = 'http://127.0.0.1:8000/api/user/email-verify' + \
                    "?token="+str(token)
                email_body = 'Hi '+user_instance.user_name + \
                    ' Use the link below to verify your email \n' + absurl
                data = {'email_body': email_body, 'to_email': user_instance.email,
                        'email_subject': 'Verify your email'}

                Util.send_email(data)

                return Response(user_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(views.APIView):
    permission_classes = [AllowAny]
    serializer_class = EmailVerificationSerializer

    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = NewUser.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetEmail(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if NewUser.objects.filter(email=email).exists():
            user = NewUser.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            # current_site = get_current_site(
            #     request=request).domain
            # relativeLink = reverse(
            #     'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            # redirect_url = request.data.get('redirect_url', '')
            absurl = 'http://127.0.0.1:8000/api/user/password-reset/' + \
                uidb64+'/'+str(token)

            email_body = 'Hello, \n Use link below to reset your password  \n' + absurl

            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            Util.send_email(data)
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request, uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = NewUser.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({'success': True, 'message': 'Credentials Valid', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Users_year(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        querySet = NewUser.objects.all()
        year = self.request.query_params.get('year')
        if year is not None:
            querySet = querySet.filter(year=year)
        return querySet


class User_profile(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        querySet = Profile.objects.all()
        user = self.request.user.id
        print(user)
        if user is not None:
            querySet = querySet.filter(user=user)
        return querySet


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class Other_user_profiles(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        id = self.kwargs['pk']
        return Profile.objects.filter(id=id)
