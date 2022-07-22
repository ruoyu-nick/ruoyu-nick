import streamlit as st
import datetime
import pytz
from simpledate import SimpleDate

st.header("Welcome to my time zone convert")

country = st.selectbox("Please select your country:",
                       options=pytz.country_names.keys())
time_zone = st.selectbox("Please select which time zone you're in:",
                         options=pytz.country_timezones(country))
time_zone = pytz.timezone(time_zone)

date = st.date_input("Select date of interest:")
time = st.time_input("Select time of interest:")
local_time = datetime.datetime.combine(date, time)

other_country = st.selectbox("Please select your other country:",
                       options=pytz.country_names.keys())
other_time_zone = st.selectbox("Please select other time zone:",
                               options=pytz.country_timezones(other_country))
other_time_zone = pytz.timezone(other_time_zone)

local_time = time_zone.localize(local_time)
other_time = SimpleDate(local_time).convert(tz=other_time_zone)
st.text('The time will be:' + other_time.datetime.ctime())
