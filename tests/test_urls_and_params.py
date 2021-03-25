import pytest

from app_logic import get_query_url

test_data = [
    ('Chicago', ({'units': 'imperial'}, 'http://api.openweathermap.org/data/2.5/weather?q=Chicago&appid=None')),
]


@pytest.mark.parametrize("location, expected", test_data)
def test_get_url_and_params(location, expected):
    assert get_query_url(location) == expected
