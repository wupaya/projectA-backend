from rest_framework import permissions
from rest_framework import status
import jwt, json
from datetime import datetime
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import HTTP_HEADER_ENCODING, exceptions
from django.utils.translation import gettext_lazy as _

class IsGetOrIsAuthenticated(permissions.BasePermission):        

    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'GET':
            return True

        # Otherwise, only allow authenticated requests
        # Post Django 1.10, 'is_authenticated' is a read-only attribute
        return request.user and request.user.is_authenticated


jwt_secret = "secret"

class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('Authorization')
        print(token)
        # if not username:
            # return None
        try:
            user = User.objects.get()
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        return (user, None)

class TokenAuthentication(authentication.BaseAuthentication):
    """
    Simple token based authentication.
    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Token ".  For example:
        Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = 'Token'
    model = None

    def get_authorization_header(self, request):
        """
        Return request's 'Authorization:' header, as a bytestring.
        Hide some test client ickyness where the header can be unicode.
        """
        auth = request.META.get('HTTP_AUTHORIZATION', b'')
        if isinstance(auth, str):
            # Work around django test client oddness
            auth = auth.encode(HTTP_HEADER_ENCODING)
        return auth

    def get_model(self):
        if self.model is not None:
            return self.model
        from rest_framework.authtoken.models import Token
        print(Token)
        return Token

    """
    A custom token model may be used, but must have the following properties.
    * key -- The string identifying the token
    * user -- The user to which the token belongs
    """

    def authenticate(self, request):
        auth = self.get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1]
        except Exception as e:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            #token = model.objects.select_related('user').get(key=key)
            token = jwt.decode(key, jwt_secret, algorithms=['HS256'])
            user = User.objects.get()
          
        except Exception as e:
            print(Exception)
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        # if not token.user.is_active:
            # raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
        return (user, token)

    def authenticate_header(self, request):
        return self.keyword
