import streamlit as st

from exceptions import InternetConnectionNotFound
from app_logic import fetch_temperature

st.title("Grabbing the Weather")
location = st.text_input('Where are you?')


def display_weather():
    try:
        fetch_and_display_results()
    except KeyError:
        remind_spellcheck()
    except InternetConnectionNotFound:
        st.write("Not Connected to the Internet!")


def remind_spellcheck():
    st.write('Could not find the city, check the spelling')
    st.write('City <State-Code> <Country-Code>')


def fetch_and_display_results():
    temperature = fetch_temperature(location=location)
    st.write(location, 'weather:')
    st.write(temperature, f'degrees Fahrenheit')


if location:
    display_weather()
