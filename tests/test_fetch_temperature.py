from unittest.mock import Mock, patch
from app import fetch_temperature


@patch('app_logic.requests.get')
def test_successful_fetch_temperature(valid_mock):
    valid_mock.return_value = {
        'main': {'temp': 66}
    }
    temperature = fetch_temperature(location='Chicago')
    assert temperature == 66


@patch('app_logic.requests.get')
def test_unsuccessful_fetch_temperature(valid_mock):
    valid_mock.return_value = {}
    try:
        fetch_temperature(location='asd')
    except KeyError:
        return True
