from unittest.mock import Mock, patch

from app_logic import make_request

valid_input = 'Chicago'
invalid_input = 'asd'


@patch('app_logic.requests.get')
def test_make_request_on_valid_input(valid_mock):
    valid_mock.return_value.status_code = 200
    response = make_request(valid_input)
    assert response.status_code == 200


@patch('app_logic.requests.get')
def test_make_request_on_invalid_input(invalid_mock):
    invalid_mock.return_value.status_code = 401
    response = make_request(invalid_input)
    assert response.status_code == 401
