import requests
from exceptions import NetworkError
from utilities import internet


def network_error_handlers(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except requests.exceptions.RequestException as e:
            if not internet():
                raise NetworkError
            raise SystemExit(1)

    return wrapper
