import streamlit as st
import numpy as np
import os

st.title("Traffic Simulator")

with st.form("my_form"):
    st.write("Parameters")
    types = ["Intersection", "Roundabout"]
    select_type = st.selectbox("Select road type", types)
    slider_val = st.slider("Vehicle Density",0,120)
    duration = st.number_input("Traffic lights duration", 10, 60)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("density : ", slider_val, "Type :", select_type, "Traffic lights Duration :", duration)
        command_ = "python twoway_intersection.py " + str(slider_val) + " " + str(duration)
        os.system(command_)