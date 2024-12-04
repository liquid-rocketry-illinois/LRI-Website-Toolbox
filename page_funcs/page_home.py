import streamlit as st

def home_page():
    st.image('images/LRI_logo.png')
    st.title("Home")
    st.logo('images/LRI_logo.png', size="large", link=None, icon_image=None)
    st.write("Welcome to LRI's Liquid Engine Analysis Toolbox")
    st.write("Website made by Alec")