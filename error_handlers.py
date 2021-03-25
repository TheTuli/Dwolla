import requests
from exceptions import InternetConnectionNotFound
from utilities import internet


def network_error_handlers(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except requests.exceptions.RequestException as e:
            if not internet():
                raise InternetConnectionNotFound
            raise SystemExit(1)

    return wrapper
