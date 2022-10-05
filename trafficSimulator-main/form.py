import streamlit as st
import numpy as np
import os

st.title("Traffic Simulator")


st.write("Parameters")
types = ["Intersection", "Roundabout"]
select_type = st.selectbox("Select road type", types)
# intersection_btn = st.button('Intersection')
# roundabout_btn = st.button('Roundabout')
slider_val = st.slider("Vehicle Density",0,120)

if select_type == 'Intersection' :
    duration = st.number_input("Traffic lights duration", 10, 60)

# Every form must have a submit button.
submitted = st.button("Submit")
if submitted:
    st.write("Type : " + select_type)
    if select_type=="Intersection" :
        command_ = "python simulation_1.py "+ str(select_type) + " " + str(slider_val) + " " + str(duration)
    else :
        
        command_ = "python simulation_1.py "+ str(select_type) + " " + str(slider_val)
    os.system(command_)