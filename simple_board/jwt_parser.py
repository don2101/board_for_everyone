import jwt
from . import settings
import datetime

second_delta = 10000

def encode(payload):
    jwt_token = jwt.encode(
        payload, \
        settings.SECRET_KEY, \
        algorithm=settings.JWT_AUTH['JWT_ALGORITHM'])

    return jwt_token


def decode(token):
    try:
        result = jwt.decode(
            token, \
            settings.SECRET_KEY, \
            algorithm=settings.JWT_AUTH['JWT_ALGORITHM'])
        
        return result
    except jwt.ExpiredSignatureError:
        return None


def set_payload(user):
    payload = {
        'id': user.id,
        'nickname': user.username,
        'email': user.email,
        'exp': datetime.datetime.now() + datetime.timedelta(seconds=second_delta)
    }

    return payload