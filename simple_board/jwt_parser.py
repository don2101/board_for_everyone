import jwt
from . import settings


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