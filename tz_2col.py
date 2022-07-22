import streamlit as st
import datetime
import pytz
from simpledate import SimpleDate
import pycountry as pyco


st.title("Welcome to Jeff's Time Zone Converter")

cols = st.columns(2)
cols[0].subheader("Your location")
cols[1].subheader("Their location")

country = cols[0].selectbox('Select your country:',
                        options=pytz.country_names.keys(),
                        index=37)
time_zone = cols[0].selectbox('Select your timezone:',
                         options=pytz.country_timezones[country])
time_zone = pytz.timezone(time_zone)

date = st.date_input('Select the date of interest:')
time = st.time_input('Enter the local time:')

local_time = datetime.datetime.combine(date, time)
local_time = time_zone.localize(local_time)

other_country = cols[1].selectbox('Select other country:',
                              options=pytz.country_names.keys())
other_time_zone = cols[1].selectbox('Select other timezone:',
                                options=pytz.country_timezones[other_country])
other_time_zone = pytz.timezone(other_time_zone)

other_time = SimpleDate(local_time).convert(tz=other_time_zone)
st.text('The time in the other location will be: ' + other_time.datetime.ctime())
