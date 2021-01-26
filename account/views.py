from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from dj_rest_auth.views import sensitive_post_parameters_m
from rest_framework.permissions import AllowAny, IsAuthenticated

from account.serializers import UserLoginSerializer


class LoginView(GenericAPIView):
    """
    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.
    Calls Django Auth login method to register User ID
    in Django session framework

    Accept the following POST parameters: username, password
    Return the REST Framework Token Object's key.
    """
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def get_response(self, token):

        response = Response(
            {
                'message': 'Logged in Successfully',
                'token': token
            },
            status=status.HTTP_200_OK
        )

        return response

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.get_response(serializer.validated_data.get('token'))
