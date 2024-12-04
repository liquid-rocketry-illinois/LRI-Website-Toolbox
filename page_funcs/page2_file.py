import streamlit as st
from analysis_funcs.regen_files.temp_contour_1 import plot_color
import csv
import pandas as pd
from analysis_funcs.regen_files.live_plot_funcs import plot_live_diff

def page20():
    st.title('Regen Channel Analysis')
    st.logo('images/LRI_logo.png', size="large", link=None, icon_image=None)
    st.write("Code Written by Andrew Park")

    uploaded_file = st.file_uploader("Upload Chamber Contour CSV:", type='csv')
    if uploaded_file is not None:
        #conver the file into the needed data
        dataframe = pd.read_csv(uploaded_file)
        x_vals = dataframe[0].to_list()  # Extract 'x' column as a list
        y_vals = dataframe[1].to_list()  # Extract 'y' column as a list

    inputs = [
        {"name": "Initial Chamber Temp (K):", "value": 3000},
        {"name": "Mach at Injector Plate:", "value": 0.25},
        {"name": "Chamber Pressure (psi):", "value": 500},
        {"name": "Input 4:", "value": 0.00}
    ]
    col1, col2 = st.columns(2)

    for i in range(0, len(inputs)):
        if i < 2:
            col1.number_input(inputs[i]["name"], value=inputs[i]["value"])
        else:
            col2.number_input(inputs[i]["name"], value=inputs[i]["value"])


    test_data = []
    with open('test_files/test_temp_contour1.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            test_data.append([float(row[0]), float(row[1]), float(row[2])])

    #add boolean to make sure all necessary files have been added correctly!
    calc_complete = False 

    data_good = True #write function to check this !

    #save plots, This is very important!
    if "plots" not in st.session_state:
        st.session_state.plots = []  # Initialize an empty list to store plots


    if len(st.session_state.plots) > 0:
        st.pyplot(st.session_state.plots[0])


    if st.button("Run Calculation"):
        #live 'redisuals'
        new_plot1 = plot_live_diff()
        st.session_state.plots.append(new_plot1)
        st.write("Calculation Complete")
        calc_complete = True
    

    st.title("Plot Results")

    if len(st.session_state.plots) > 1:
        st.pyplot(st.session_state.plots[1])
    
    if st.button("Plot Temperature Data"):
            new_plot2 = plot_color(test_data)
            st.pyplot(new_plot2)
            st.session_state.plots.append(new_plot2)
    
    


