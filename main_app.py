import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
from mpmath import sec
from math import *
import matplotlib.pyplot as plt
from analysis_funcs.chamber_files.chamber_size import calc_size_chamber
from analysis_funcs.chamber_files.chamber_plotter import polt_chamber_contour
import pandas as pd
from api_ref.api_regen import get_regen_string
from page_funcs.page1_file import page10
from page_funcs.page2_file import page20
from page_funcs.page3_file import page30
from page_funcs.page4_file import page40
from page_funcs.page_home import home_page

page10_title = 'Thrust Chamber Design'
page20_title = 'Regen Channel Analysis'
page30_title = "API Reference"
page40_title = "Pintle Injector Sizing"

# Main function
def main():
    # Sidebar navigation menu
    with st.sidebar:
        menu_option = option_menu(
            "LRI Engine Analysis Toolbox",
            ["Home", page10_title, page20_title, page40_title, page30_title],
            icons=["house", "file", "file", "file", "file"],
            menu_icon="none",
            default_index=0,
        )

    # Route based on selection
    if menu_option == "Home":
        home_page()
    elif menu_option == page10_title:
        page10()
    elif menu_option == page20_title:
        page20()
    elif menu_option == page30_title:
        page30()
    elif menu_option == page40_title:
        page40()

# Run the app
if __name__ == "__main__":
    main()

# python -m streamlit run main_app.py