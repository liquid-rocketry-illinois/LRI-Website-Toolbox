import streamlit as st
from api_ref.api_regen import get_regen_string

def api_regen():
    st.title('Regen API Reference Page')
    st.logo('images/LRI_logo.png', size="large", link=None, icon_image=None)
    
    st.latex(r'''
    q = h_{gas}(T_{aw} - T_{hw})
    ''')

    markdown_string = get_regen_string('string1')
    st.markdown(markdown_string)

def api_chamber():
    st.title('Chamber Sizing API Reference Page')
    st.logo('images/LRI_logo.png', size="large", link=None, icon_image=None)
    
def api_pintle():
    st.title('Pintle Injector API Reference Page')
    st.logo('images/LRI_logo.png', size="large", link=None, icon_image=None)
    
