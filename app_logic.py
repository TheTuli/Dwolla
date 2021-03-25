import requests
from config import BASE_URL, ACCESS_KEY, UNITS

from error_handlers import network_error_handlers


@network_error_handlers
def make_request(location):
    query_url = get_query_url(location=location)
    return requests.get(url=query_url)


def get_query_url(location):
    search_query = ','.join(location.split())
    return f"{BASE_URL}?q={search_query}&appid={ACCESS_KEY}&units={UNITS}"


def get_dict(response):
    # assert response
    return response.json()


def extract_temperature(response_body):
    # assert response_body
    # assert response_body['main']
    # assert response_body['main']['temp']

    temperature = response_body['main']['temp']
    return temperature


def fetch_temperature(location):
    response = make_request(location=location)
    return extract_temperature(get_dict(response))
