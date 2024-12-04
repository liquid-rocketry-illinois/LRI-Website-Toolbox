import streamlit as st
from page_funcs.api_pages.api_page_all import api_chamber, api_pintle, api_regen
from streamlit_option_menu import option_menu

def page30():
    page10_title = 'Thrust Chamber Design'
    page20_title = 'Regen Channel Analysis'
    page30_title = "API Reference"
    page40_title = "Pintle Injector Sizing"

    #st.title(page30_title)
    st.logo('images/LRI_logo.png', size="large", link=None, icon_image=None)
    #add multiple sections
    with st.sidebar:
        options = option_menu(
            "API Reference Page",
            [page10_title, page20_title, page40_title],
            icons = ['file', 'file', 'file'],
            menu_icon='none',
            default_index=0
            )
    if options == page20_title:
        api_regen()
    elif options == page40_title:
        api_pintle()
    elif options == page10_title:
        api_chamber()

