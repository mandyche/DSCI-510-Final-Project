import streamlit as st
import pandas as pd

st.set_page_config(page_title='Multipage App')

#Sidebar and title setup
st.title('Mandy Chen - DSCI 510 Final Project')
st.sidebar.success('Select a page above.')

#Main page written
st.write('Hello! Welcome to my research project about discovering the correlational relationship between weather, financial news, and stock performance. In this project, my ultimate goal is to investigate the potential relationship between financial news sentiment, weather patterns, and stock performance. I scraped all of 2023 BBC business news title and put them into chatgpt asking for the impact rating (if there are 7 news that day, 4 out of 7 news titles considered as positive, then the overall rating for the news during that day is rated as positive). I also simplified the weather rating into rainy and sunny only. If the weather that day is not rainy(cloudy or partly cloudy), it is considered as sunny. By analyzing these datasets and compare with SPY stock performance, I hope I could provide valuable insights for investors and analysts in understanding market dynamics.')
st.write('In this webapp, I have this interactivity where you could use the sidebar radio to see the result of stock performance by adjusting weather filter and news title impact filters.')
st.write('A major "gotcha" in this project is that I am not able to highlight the graph with filtered parts. My initial thought was to create a highlighter over my displayed graph. For example, if I adjust the weather filter to be rainy and news rating impact to be positive, I want highlights on the graph indicating the parts where the filteres are applied instead of only shsowing the filtered parts.')