from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

import firebase_admin
from firebase_admin import credentials, auth

from .serializers import AuthenticationSerializer, TokenSerializer

firebase_admin.initialize_app()


class AuthenticateView(APIView):
    """
    Fetch the cutom JWT

    - Requires fireestore account to run
    - Requires User with id 1 if using fixtures provided
    - Loaddata from provided fixtures
    """

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        serializer = AuthenticationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:

                additional_claims = {
                    'tenant': user.userprofile.tenant.id
                }
                custom_token = auth.create_custom_token(
                    str(user.id), additional_claims)

                ts = TokenSerializer({'token': custom_token})
                return Response(ts.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
