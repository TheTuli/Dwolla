import streamlit as st
import requests
from config import ACCESS_KEY

url = 'http://api.openweathermap.org/data/2.5/weather'

st.title("Rahul's Technical Exercise")

location = st.text_input('Enter your location?')

if location:
    query_url = f"{url}?q={location}&appid={ACCESS_KEY}"

    params = {
        'units': 'imperial'
    }
    r = requests.get(url=query_url, params=params)
    st.write(f"{location} weather:")
    temp = r.json()['main']['temp']
    st.write(f"{temp} degrees Fahrenheit")


