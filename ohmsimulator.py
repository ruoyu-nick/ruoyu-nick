# -*- coding: utf-8 -*-
"""
Created on Mon May 23 14:15:40 2022

@author: Ruoyu Dong
"""

import streamlit as st
from bokeh.plotting import figure


st.title("Wellcome to Ruoyu's Ohm simulator")

volatage= st.number_input("Please choose your wanted voltage")

st.write("Now your overall voltage will be", volatage, 'V')

resistance_1=st.slider("Please chooose a value of your First resistor", min_value=0, max_value=1000)

st.write("Now your First resistor will be", resistance_1,'\u03A9')

resistance_2=st.select_slider("Please chooose a value of your Second resistor", options=range(1001))

st.write("Now your Second resistor will be", resistance_2,'\u03A9')

def show_num(): 
    if resistance_1+resistance_2==0 :
        st.write("Please slide a value for your resistor")
    else:
        current= volatage/(resistance_1+resistance_2)
        st.write("Now in the circuit, the current is", current,'A')

show_num()
def current():
    if resistance_1+resistance_2==0:
        return None
    if resistance_1+resistance_2!=0:
        return volatage/(resistance_1+resistance_2)
    
col1, col2, col3 = st.columns(3)
col1.metric("Voltage", volatage)
col2.metric("Overall resistance", resistance_1+resistance_2)
col3.metric("Current", current())

st.text('This is the plot that how the volatage drop when it goes through the circuit')


x = [current()]
y = [volatage]

p = figure(
     title='Voltage',
     x_axis_label='x',
     y_axis_label='y')

p.line(x, y, legend_label='Voltage', line_width=2)

st.bokeh_chart(p, use_container_width=True)


