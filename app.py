import streamlit as st
import requests
from config import ACCESS_KEY

url = 'http://api.openweathermap.org/data/2.5/weather'

st.title("Rahul's Technical Exercise")

location = st.text_input('Enter your location?')


def get_temp(location):
    params, query_url = get_url_and_params(location)
    response_body = requests.get(url=query_url, params=params)
    return extract_temperature(response_body.json())


def extract_temperature(response_body):
    temperature = response_body['main']['temp']
    return temperature


def get_url_and_params(location):
    query_url = f"{url}?q={location}&appid={ACCESS_KEY}"
    params = {
        'units': 'imperial'
    }
    return params, query_url


if location:
    temp = get_temp(location)
    st.write(f"{location} weather (Fahrenheit):")
    st.write(temp)

