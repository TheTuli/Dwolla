from app import extract_temperature


def test_extract_temperature_when_valid_body():
    test_response_body = {
        'main': {'temp': 60}
    }
    assert extract_temperature(test_response_body) == 60


def test_key_error_in_extract_temperature_when_invalid_body():
    test_response_body = {
        'main': {}
    }
    try:
        extract_temperature(test_response_body)
        assert False
    except KeyError:
        assert True

