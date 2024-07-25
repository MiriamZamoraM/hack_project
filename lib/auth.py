import requests

from core.settings import CONFIG
from lib.exceptions import TokenException


def get_token(email: str, password: str):
    try:
        token = requests.post(
            f'{CONFIG["SELF_HOST"]}/o/token/',
            data={
                "grant_type": "password",
                "username": email,
                "password": password,
                "client_id": CONFIG["OAUTH_CLIENT_ID"],
                "client_secret": CONFIG["OAUTH_CLIENT_SECRET"],
            },
        )

        return token
    except TokenException:
        raise TokenException(message="Ha ocurrido un error al generar token")
