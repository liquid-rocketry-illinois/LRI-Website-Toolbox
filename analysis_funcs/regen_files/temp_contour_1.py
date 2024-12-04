import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

def plot_color(list):
    x = [item[0] for item in list]
    y = [item[1] for item in list]
    temperature = [item[2] for item in list]

    fig, ax = plt.subplots(figsize=(14, 6)) 

    # First subplot
    scatter1 = ax.scatter(x, y, c=temperature, cmap='jet', s=120, edgecolor=None)
    ax.set_title("Temperature Along Chamber and Nozzle Wall")
    fig.colorbar(scatter1, ax=ax, label="Temperature (K)")  # Add colorbar for this subplot
    ax.set_aspect("equal", adjustable="datalim")
    ax.set_ylim(bottom=0)
    ax.grid(False)

    return fig