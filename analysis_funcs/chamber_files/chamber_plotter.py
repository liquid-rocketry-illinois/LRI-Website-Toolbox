import numpy as np
from mpmath import sec
from math import *
import matplotlib.pyplot as plt
import streamlit as st

def polt_chamber_contour(x, y):
    fig, ax = plt.subplots(figsize=(20, 6))

    # Plot the data
    ax.plot(x, y, color="blue", linewidth=3)  # Blue line, thicc

    # Customize the plot
    ax.set_facecolor("white")  # White background
    ax.grid(False)  # No gridlines
    ax.set_aspect("equal", adjustable="datalim")
    ax.set_ylim(bottom=0)
    
    # Display the plot
    return fig