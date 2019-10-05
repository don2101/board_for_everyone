from simple_board import jwt_parser
from django.contrib.auth import get_user_model


def is_authenticated(token):
    result = jwt_decode(token)

    if result: return True
    else: return False


def jwt_decode(token):
    result = jwt_parser.decode(token)
    
    return result


def get_user(pk):
    User = get_user_model()

    return User.objects.get(pk=pk)