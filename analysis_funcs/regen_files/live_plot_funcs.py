import streamlit as st
import matplotlib.pyplot as plt
import time
import numpy as np

def plot_live_diff(): #does live plot and returns final frame 
    plot_container = st.empty()
    
    # Initialize the figure
    fig, ax = plt.subplots()

    # Initialize data storage for 6 lines
    num_iterations = 10
    x_data = list(range(1, num_iterations + 1))
    y_data = {i: [] for i in range(6)}

    # Live plotting
    for i in range(1, num_iterations + 1):
        # Generate 6 random numbers
        random_values = np.random.randint(25, 100-(i*5), 6)
        for j in range(6):
            y_data[j].append(random_values[j])

        # Clear the plot
        ax.clear()
        
        # Plot all 6 lines
        for j in range(6):
            ax.plot(x_data[:i], y_data[j], label=f"Line {j+1}")
        
        # Customize the plot
        ax.set_title("Live Plot of Random Numbers")
        ax.set_xlabel("Iteration")
        ax.set_ylabel("Random Value")
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.6)

        # Render the plot in the container
        plot_container.pyplot(fig)
        
        # Pause to simulate live plotting
        time.sleep(0.5)
    
    final_fig = fig
    return final_fig

