import streamlit as st
from analysis_funcs.chamber_files.chamber_size import calc_size_chamber
from analysis_funcs.chamber_files.chamber_plotter import polt_chamber_contour
import pandas as pd 

def page10():
    st.image('images/Unity_pic.png')
    st.title('Thrust Chamber Design')
    st.logo('images/LRI_logo.png', size="large", link=None, icon_image=None)
    st.write("Code Written By Andrew K and Zach Yashar")
    st.write("Please fill in all of the following values:")
    st.write("DATA WILL BE LOST IF YOU SWITCH TO ANOTHER TAB!")
    col1, col2 = st.columns(2)
    #variables
    thrust = col1.number_input("1- Thrust (N):", min_value=0.01, value=1000.0)
    of_r = col1.number_input("2 - OF Ratio:", min_value=0.01, value=3.0)
    c_pressure = col1.number_input("3 - Chamber Pressure (psi):", min_value=0.01, value=500.0)
    e_pressure = col1.number_input("4 - Exit Pressure (atm) :", min_value=0.01, value=0.5)
    l_star = col1.number_input("5 - Characteristic Length (m):", min_value=0.01, value=1.0)

    chamber_temp = col2.number_input("6 - Chamber Temperature (K):", min_value=0.01, value=3000.0)
    cp = col2.number_input("7 - Specific Heat of Chamber (kJ/kg*K) :", min_value=0.01, value=4.5)
    gamma = col2.number_input("8 - Ratio of Specific Heats :", min_value=0.01, value=1.2)
    isp_ms = col2.number_input("9 - ISP (m/s):", min_value=0.01, value=3000.0)
    m_exit = col2.number_input("10 - Exit Mach Number  :", min_value=0.01, value=3.5)
    exp_r = col2.number_input("11 - Ae/At Expansion Ratio :", min_value=0.01, value=7.0)
    
    file_name1 = st.text_input("In order to downolad the contour CSV, please enter a file name:")
    file_name2 = file_name1 + ".csv"

    csv_chamber = 0.00
    can_down  = False

    #save plots, This is very important!
    if "plots" not in st.session_state:
        st.session_state.plots = []  # Initialize an empty list to store plots

    if "vals" not in st.session_state:
        st.session_state.vals = []
    

    #call function that generates chamber
    if st.button("Compute Chamber Contour"):
        x_chamber, y_chamber = calc_size_chamber(
            thrust, 
            of_r, 
            c_pressure, 
            e_pressure, 
            l_star, 
            chamber_temp, 
            cp, 
            gamma, 
            isp_ms, 
            m_exit, 
            exp_r
            )
        val_list = [
            thrust, 
            of_r, 
            c_pressure, 
            e_pressure, 
            l_star, 
            chamber_temp, 
            cp, 
            gamma, 
            isp_ms, 
            m_exit, 
            exp_r
        ]
        #create the fig and plot it 
        contour_plot = (polt_chamber_contour(x_chamber, y_chamber))
        st.pyplot(contour_plot)
        #create the string assosiated with inputs
        values = "{"
        for i in range(11):
            values += ' ' + str(i+1) + ":" + str(val_list[i]) + ','
        values += '}'

        #save the plot and input values assositated with it 
        st.session_state.plots.append(contour_plot)
        st.session_state.vals.append(values)

        st.write("Calculation Complete")

        #convert to downloadable csv
        df = pd.DataFrame({"X": x_chamber, "Y": y_chamber})
        csv_chamber = df.to_csv(index=False)
        can_down = True

    if can_down:
        #save as a csv file with name

        # Create a download button
        st.download_button(
            label="Download CSV of Chamber",
            data = csv_chamber,
            file_name = file_name2,
            mime="text/csv"
        )
        
    st.title("Previous Contours and Values")

    if len(st.session_state.plots) > 0:
        for i in range(len(st.session_state.plots) - 1, 0): #why does this not work ??
            st.write(st.session_state.vals[i])
            st.pyplot(st.session_state.plots[i])