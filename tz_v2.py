import streamlit as st
import datetime
import pytz
from simpledate import SimpleDate
import pycountry as pyco


st.title("Welcome to Jeff's Time Zone Converter")

country = st.text_input('Enter the country you are in now:', value='Canada')
country = pyco.countries.lookup(country).alpha_2
time_zone = st.selectbox('Select your timezone:',
                          options=pytz.country_timezones[country])
time_zone = pytz.timezone(time_zone)

date = st.date_input('Select the date of interest:')
time = st.time_input('Enter the local time:')

local_time = datetime.datetime.combine(date, time)
local_time = time_zone.localize(local_time)

other_country = st.text_input('Enter the other country:', value='China')
other_country = pyco.countries.lookup(other_country).alpha_2
other_time_zone = st.selectbox('Select other timezone:',
                                options=pytz.country_timezones[other_country])
other_time_zone = pytz.timezone(other_time_zone)

other_time = SimpleDate(local_time).convert(tz=other_time_zone)
st.text('The time in the other location will be: ' + other_time.datetime.ctime())
