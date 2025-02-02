from datetime import datetime, timedelta
from backend.models import *
from .exceptions import *
from backend.helpers import *
from .users import *
from backend.models import *
from secrets import token_hex
from .medsenger_api import *
from .clinics import *
from backend.config import MEDSENGER_LOGIN

def authorize_by_credentials(email, password):
    if not email or not password:
        raise InsufficientData

    if MEDSENGER_LOGIN:
        medsenger_user = medsenger_login_user(email, password)
        user = find_user_by_email(email)

        if not user:
            medsenger_clinic = medsenger_user['clinics'][0]
            clinic = find_clinic_by_id(medsenger_clinic['id'])
            user = create_user(email, password, medsenger_user['name'], clinic)
    else:
        user = find_user_by_email(email)
        if not user:
            raise NotFound

        if user.password != hash(password):
            raise IncorrectPassword

    return user, create_token(user)


def authorize(user):
    return create_token(user)


def check_password(user, password):
    return user.password == hash(password)


def find_user_by_token(token):
    if not token:
        raise NoToken

    token = UserToken.query.filter_by(token=token).first()

    if not token:
        raise IncorrectToken

    if token.expire_on < datetime.now():
        raise ExpiredToken

    return token.user


@transaction
def create_token(user):
    token = UserToken(user_id=user.id)
    token.expire_on = datetime.now() + timedelta(days=7)
    token.token = token_hex(16)

    db.session.add(token)
    return token


def requires_user(func):
    def wrapper(*args, **kwargs):
        token = request.args.get('api_token')
        user = find_user_by_token(token)
        result = func(user, *args, **kwargs)
        return result

    wrapper.__name__ = func.__name__
    return wrapper
