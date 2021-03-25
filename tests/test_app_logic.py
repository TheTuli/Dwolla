from app_logic import make_request, extract_temperature, fetch_temperature
from exceptions import InternetConnectionNotFound
from utilities import internet


def test_make_request():
    dummy_loc = 'Chicago'
    make_request(dummy_loc)


def test_extract_temperature():
    dummy_response_dict = {
        'main': {
            'temp': 60
        }
    }
    assert extract_temperature(dummy_response_dict) == 60


def test_extract_temperature_with_invalid_body():
    invalid_body = {
        'main': {
        }
    }

    try:
        extract_temperature(invalid_body)
    except AssertionError:
        return True

