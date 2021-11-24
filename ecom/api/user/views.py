from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import exceptions
from .serializers import UserSerializer
from .authentication import JWTAuthentication
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
import jwt
import json
from ..auth import secret_key

class RegisterApiView(APIView):
    def post(self, request):
        data = request.data
        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Password dont match')

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            "resultCode": "0"
        }
        return response



class LoginApiView(APIView):
    def post(self, request):
        data = request.data

        email = data['email']
        password = data['password']
        response = Response()
        user = CustomUser.objects.filter(email=email).first()
        if user is None:
            response.data = {
                "resultCode": "10"
            }
            return response

        if not user.check_password(password):
            response.data = {
                "resultCode": "10"
            }
            return response

        token = JWTAuthentication.generate_jwt(user.id)


        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            "resultCode": "0"
        }
        return response


class UserAPIView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, _):
        response = Response()
        response.delete_cookie(key='jwt')
        response.data = {
            "resultCode": "0"
        }
        return response


class CheckAuthUser(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):

        token = request.COOKIES.get('jwt')

        if not token:
            return Response({"resultCode": "10"})

        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('unauthenticated')

        user = CustomUser.objects.get(pk=payload['user_id'])

        if user is None:
            return Response({"resultCode": "10"})
            # raise exceptions.AuthenticationFailed('User not found')

        return Response({"resultCode": "0", "data":UserSerializer(user).data})