import streamlit as st
import pandas as pd


import matplotlib.pyplot as plt
import numpy as np

# Load my dataframe
spy = pd.read_csv("spy_2023_pricing.csv")

# Ensure 'Date' column is in datetime format
spy['Date'] = pd.to_datetime(spy['Date'])

# Specify "plot", so get a line plot
def plot_graph(data, title):
    plt.plot(data['Date'], data['Closing Price'])
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('SPY Closing')
    st.set_option('deprecation.showPyplotGlobalUse', False) #disable warning by disabling the config option
    st.pyplot()


# Sidebar filtered buttons
selected_weather = st.sidebar.radio("Select Weather:", ['All', 'Sunny', 'Rainy'])
selected_impact = st.sidebar.radio("Select Impact:", ['All', 'Positive', 'Negative'])

# Filter DataFrame based on selected options
if selected_weather == 'All' and selected_impact == 'All':
    filtered_spy = spy
elif selected_weather == 'All':
    filtered_spy = spy[spy['News Rating'] == selected_impact.capitalize()]
elif selected_impact == 'All':
    filtered_spy = spy[spy['Weather'] == selected_weather]
else:
    filtered_spy = spy[(spy['Weather'] == selected_weather) & (spy['News Rating'] == selected_impact.capitalize())]

# Visualize my dataframe in the Streamlit app
st.write(filtered_spy)

# Plot the line graph with filtered data
plot_graph(filtered_spy, f"Stock Price - Weather: {selected_weather}, News Rating: {selected_impact}")

