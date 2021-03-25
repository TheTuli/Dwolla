import streamlit as st
import requests
from config import ACCESS_KEY

url = 'http://api.openweathermap.org/data/2.5/weather'

st.title("Rahul's Technical Exercise")

location = st.text_input('Enter your location?')


def get_temp(location):
    query_url = f"{url}?q={location}&appid={ACCESS_KEY}"
    params = {
        'units': 'imperial'
    }
    r = requests.get(url=query_url, params=params)
    temperature = r.json()['main']['temperature']
    return temperature


if location:
    temp = get_temp(location)
    st.write(f"{location} weather:")
    st.write(f" {temp} Fahrenheit")
