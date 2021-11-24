import jwt, datetime
# from ecom.api.auth import *
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .models import CustomUser
from ..auth import secret_key

class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            return None

        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('unauthenticated')

        user = CustomUser.objects.get(pk=payload['user_id'])

        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        return (user, None)

    @staticmethod
    def generate_jwt(id):
        payload = {
            "user_id": id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow()
        }
        return jwt.encode(payload, secret_key, algorithm='HS256')
