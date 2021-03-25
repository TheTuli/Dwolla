from app_logic import extract_temperature

valid_response_for_temp_extraction = {
    'main': {
        'temp': 60
    }
}

invalid_response_for_temp_extraction = {
    'main': {
    }
}


def test_temperature_extraction_on_a_valid_response():
    assert extract_temperature(valid_response_for_temp_extraction) == 60


def test_extract_temperature_on_invalid_response():
    try:
        extract_temperature(invalid_response_for_temp_extraction)
    except KeyError:
        return True
